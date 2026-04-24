from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from app.core.database import get_session
from app.models.lottery import DrawsList,BingoExtra
from app.schemas.lottery import DrawResponse, LatestDrawsResponse,BingoResponse
from app.core.security import verify_api_key
router = APIRouter()

GAMES_WITH_SPECIAL = {5118, 5134}
def get_special(game_code:int,numbers:list[int])-> int | None:
    if game_code in GAMES_WITH_SPECIAL:
        return numbers[-1]
    return None

@router.get("/latest", response_model=LatestDrawsResponse,dependencies=[Depends(verify_api_key)])
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
        special = get_special(draw.game_code, draw.numbers)
        numbers = draw.numbers[:-1] if special is not None else draw.numbers
        draw_list.append(DrawResponse(
            game_code=draw.game_code,
            term=draw.term,
            draw_date=draw.draw_date,
            numbers=numbers,
            special=special,
            next_draw_date=draw.next_draw_date,
        ))

    return LatestDrawsResponse(draws=draw_list)

@router.get('/bingo/latest', response_model = BingoResponse,dependencies=[Depends(verify_api_key)])
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
        special=int(extra.lot_special),
        lot_big_small=extra.lot_big_small,
        lot_odd_even=extra.lot_odd_even,
    )
