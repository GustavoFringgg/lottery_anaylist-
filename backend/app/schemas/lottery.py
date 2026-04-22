from pydantic import BaseModel
from datetime import datetime


class DrawResponse(BaseModel):
    game_code: int
    term: str
    draw_date: datetime
    numbers: list[int]
    next_draw_date: datetime | None


class BingoResponse(BaseModel):
    game_code: int
    term: str
    draw_date: datetime
    numbers: list[int]
    next_draw_date: datetime | None
    lot_special: str
    lot_big_small: str
    lot_odd_even: str


class LatestDrawsResponse(BaseModel):
    draws: list[DrawResponse]
