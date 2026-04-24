from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from app.core.database import get_session
from app.models.lottery import DrawsList,BingoExtra,Game
from app.schemas.lottery import DrawResponse, DrawHistoryItem, BingoDrawHistoryItem, BingoResponse, DrawListResponse
from app.core.security import verify_api_key
router = APIRouter()

GAMES_WITH_SPECIAL = {5118, 5134}
def get_special(game_code:int,numbers:list[int])-> int | None:
    if game_code in GAMES_WITH_SPECIAL:
        return numbers[-1]
    return None

@router.get("/latest", response_model=list[DrawResponse], dependencies=[Depends(verify_api_key)])
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

    return draw_list

@router.get("/draws/{slug}",response_model = DrawListResponse,dependencies=[Depends(verify_api_key)])
async def get_draws_by_slug(
    slug:str,limit:int=10,
    db: AsyncSession = Depends(get_session)):

    limit = min(limit,30)
    game_result = await db.execute(select(Game).where(Game.slug == slug))
    game = game_result.scalars().first()
    if game is None:
        raise HTTPException(status_code = 404, detail='not found game')
    if game.game_code == 1102:
        result = await db.execute(
            select(DrawsList,BingoExtra)
            .join(BingoExtra,BingoExtra.draw_id == DrawsList.id)
            .where(DrawsList.game_code == 1102)
            .order_by(desc(DrawsList.draw_date))
            .limit(limit)
        )
        draw_list = []
        for draw, extra in result.all():
            special = int(extra.lot_special)
            draw_list.append(BingoDrawHistoryItem(
                game_code=draw.game_code,
                term=draw.term,
                draw_date=draw.draw_date,
                numbers=draw.numbers,
                special=special,
                lot_big_small=extra.lot_big_small,
                lot_odd_even=extra.lot_odd_even,
            ))
    else:
        draws_result = await db.execute(
            select(DrawsList)
            .where(DrawsList.game_code == game.game_code)
            .order_by(desc(DrawsList.draw_date))
            .limit(limit)
        )
        draws = draws_result.scalars().all()

        draw_list = []
        for draw in draws:
            special = get_special(draw.game_code, draw.numbers)
            numbers = draw.numbers[:-1] if special is not None else draw.numbers
            draw_list.append(DrawHistoryItem(
                game_code=draw.game_code,
                term=draw.term,
                draw_date=draw.draw_date,
                numbers=numbers,
                special=special,
            ))
        
    return DrawListResponse(
        slug = game.slug,
        name = game.name,
        draw_list = draw_list
    )


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
