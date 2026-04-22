from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from app.core.database import get_session
from app.models.lottery import DrawsList,BingoExtra
from app.schemas.lottery import DrawResponse, LatestDrawsResponse,BingoResponse

router = APIRouter()


@router.get("/latest", response_model=LatestDrawsResponse)
async def get_latest(db: AsyncSession = Depends(get_session)):
    result = await db.execute(
        select(DrawsList)
        .where(DrawsList.game_code != 1102)
        .distinct(DrawsList.game_code)
        .order_by(DrawsList.game_code, desc(DrawsList.draw_date))
    )
    draws = result.scalars().all()

    draw_list = []
    for draw in draws:
        draw_list.append(DrawResponse(
            game_code=draw.game_code,
            term=draw.term,
            draw_date=draw.draw_date,
            numbers=draw.numbers,
            next_draw_date=draw.next_draw_date,
        ))

    return LatestDrawsResponse(draws=draw_list)

@router.get('/bingo/latest', response_model = BingoResponse )
async def get_latest_bingo(db:AsyncSession = Depends(get_session)):
    result = await db.execute(
        select(DrawsList, BingoExtra)
        .join(BingoExtra, BingoExtra.draw_id == DrawsList.id)
        .where(DrawsList.game_code == 1102)
        .order_by(desc(DrawsList.draw_date))
        .limit(1)
    )
    row = result.first()
    if row is None:
        raise HTTPException(status_code=404, detail="尚無 BingoBingo 開獎資料")
    draw, extra = row
    return BingoResponse(
        game_code=draw.game_code,
        term=draw.term,
        draw_date=draw.draw_date,
        numbers=draw.numbers,
        next_draw_date=draw.next_draw_date,
        lot_special=extra.lot_special,
        lot_big_small=extra.lot_big_small,
        lot_odd_even=extra.lot_odd_even,
    )
