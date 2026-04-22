from sqlalchemy.ext.asyncio import AsyncSession
from app.models.lottery import DrawsList, BingoExtra
from sqlalchemy import select

async def save_draws(session: AsyncSession, draws: list[dict]):
    for draw in draws:
        existing = await session.execute(
            select(DrawsList).where(
                DrawsList.game_code == draw["game_code"],
                DrawsList.term == draw["term"]
            )
        )
        if existing.scalar_one_or_none() is not None:
            continue

        row = DrawsList(
            game_code=draw["game_code"],
            term=draw["term"],
            draw_date=draw["draw_date"],
            numbers=draw["numbers"],
            next_draw_date=draw["next_draw_date"],
        )
        session.add(row)
        await session.flush()  # 取得 row.id 
        if draw["game_code"] == 1102:
            extra = BingoExtra(
                draw_id=row.id,
                lot_special=draw["lot_special"],
                lot_big_small=draw["lot_big_small"],
                lot_odd_even=draw["lot_odd_even"],
            )
            session.add(extra)

    await session.commit()