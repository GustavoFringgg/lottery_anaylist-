import json
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, text

from core.database import get_db
from core.redis_client import get_redis
from core.ws_manager import ws_manager
from models.lottery import DrawResult
from schemas.lottery import DrawResultResponse, HotNumber, HistoryResponse

router = APIRouter(prefix="/api/lottery", tags=["lottery"])

CACHE_TTL = 30  # seconds


@router.get("/latest", response_model=DrawResultResponse)
async def get_latest(db: AsyncSession = Depends(get_db)):
    redis = await get_redis()

    # Try cache first
    cached = await redis.get("latest_draw")
    if cached:
        return json.loads(cached)

    result = await db.execute(
        select(DrawResult).order_by(DrawResult.draw_date.desc()).limit(1)
    )
    draw = result.scalar_one_or_none()

    if not draw:
        return DrawResultResponse(
            draw_term="--",
            draw_date="--",
            numbers=[],
            special_number=None,
        )

    data = DrawResultResponse(
        draw_term=draw.draw_term,
        draw_date=str(draw.draw_date),
        numbers=draw.numbers,
        special_number=draw.special_number,
        source=draw.source,
    )
    await redis.setex("latest_draw", CACHE_TTL, data.model_dump_json())
    return data


@router.get("/history", response_model=HistoryResponse)
async def get_history(limit: int = 10, offset: int = 0, db: AsyncSession = Depends(get_db)):
    total_res = await db.execute(select(func.count()).select_from(DrawResult))
    total = total_res.scalar()

    result = await db.execute(
        select(DrawResult)
        .order_by(DrawResult.draw_date.desc())
        .offset(offset)
        .limit(limit)
    )
    draws = result.scalars().all()

    records = [
        DrawResultResponse(
            draw_term=d.draw_term,
            draw_date=str(d.draw_date),
            numbers=d.numbers,
            special_number=d.special_number,
            source=d.source,
        )
        for d in draws
    ]
    return HistoryResponse(records=records, total=total or 0)


@router.get("/hot-numbers", response_model=list[HotNumber])
async def get_hot_numbers(periods: int = 30, db: AsyncSession = Depends(get_db)):
    redis = await get_redis()
    cache_key = f"hot_numbers:{periods}"
    cached = await redis.get(cache_key)
    if cached:
        return json.loads(cached)

    # Unnest numbers array and count occurrences
    query = text("""
        WITH recent AS (
            SELECT unnest(numbers) AS num
            FROM draw_results
            ORDER BY draw_date DESC
            LIMIT :periods
        )
        SELECT num, COUNT(*) AS cnt
        FROM recent
        GROUP BY num
        ORDER BY cnt DESC
        LIMIT 10
    """)
    result = await db.execute(query, {"periods": periods})
    rows = result.fetchall()

    max_count = rows[0][1] if rows else 1
    hot = [
        HotNumber(
            number=row[0],
            count=row[1],
            percentage=round(row[1] / max_count * 100, 1),
        )
        for row in rows
    ]

    await redis.setex(cache_key, 300, json.dumps([h.model_dump() for h in hot]))
    return hot


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            # Keep connection alive; server pushes via ws_manager.broadcast()
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
