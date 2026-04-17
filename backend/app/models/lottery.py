from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import datetime,date

class DrawsList(SQLModel, table = True):
    id: Optional[int] = Field(default = None,primary_key = True)
    game_code: str 
    game_name: str 
    term:str 
    draw_date:date
    next_draw_date:date
    special_number: Optional[int] = None 
    created_at: datetime = Field(default_factory=datetime.utcnow)

class DrawNumbers(SQLModel,table = True):
    id: Optional[int] = Field(default = None,primary_key = True)
    draw_id:int = Field(foreign_key = 'drawslist.id')
    number:int
