from pydantic import BaseModel
from datetime import datetime

# 每筆樂透的資料結構
class DrawResponse(BaseModel):
    game_code: int
    term: str
    draw_date: datetime
    numbers: list[int]
    special: int | None
    next_draw_date: datetime | None

# BingoBingo 的資料結構
class BingoResponse(BaseModel):
    game_code: int
    term: str
    draw_date: datetime
    numbers: list[int]
    next_draw_date: datetime | None
    special: int
    lot_big_small: str
    lot_odd_even: str



# 單一樂透的歷史資料資料結構
class DrawHistoryItem(BaseModel):
    game_code: int
    term: str
    draw_date: datetime
    numbers: list[int]
    special: int | None

# BingoBingo 的歷史資料資料結構
class BingoDrawHistoryItem(DrawHistoryItem):
    lot_big_small: str
    lot_odd_even: str

# 回給前端單一種類彩券歷史資料的資料結構
class DrawListResponse(BaseModel):
    slug: str
    name: str
    draw_list: list[DrawHistoryItem | BingoDrawHistoryItem]
