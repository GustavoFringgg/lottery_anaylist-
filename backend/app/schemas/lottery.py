from pydantic import BaseModel
from datetime import date
from typing import Optional


class DrawResultResponse(BaseModel):
    draw_term: str
    draw_date: str
    next_draw_date: Optional[str] = None
    numbers: list[int]
    special_number: Optional[int]
    is_live: bool = False
    source: Optional[str] = None

    class Config:
        from_attributes = True


class HotNumber(BaseModel):
    number: int
    count: int
    percentage: float


class HistoryResponse(BaseModel):
    records: list[DrawResultResponse]
    total: int
