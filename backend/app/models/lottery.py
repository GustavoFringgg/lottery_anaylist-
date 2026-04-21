from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ARRAY, INTEGER
from typing import Optional, List
from datetime import datetime, date


class Game(SQLModel, table=True):
    game_code: int = Field(primary_key=True)
    name: str


class DrawsList(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    game_code: int = Field(foreign_key="game.game_code")
    term: str
    draw_date: date
    next_draw_date: Optional[datetime] = None
    numbers: List[int] = Field(sa_column=Column(ARRAY(INTEGER)))
    source: str = Field(default="api")
    is_verified: bool = Field(default=False)
    verified_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BingoExtra(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    draw_id: int = Field(foreign_key="drawslist.id")
    lot_special: int
    lot_big_small: str
    lot_odd_even: str


class DrawDiscrepancy(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    draw_id: int = Field(foreign_key="drawslist.id")
    api_numbers: str
    official_numbers: str
    api_special: Optional[int] = None
    official_special: Optional[int] = None
    detected_at: datetime = Field(default_factory=datetime.utcnow)
