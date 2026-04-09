from sqlalchemy import Column, Integer, String, Date, ARRAY, Boolean, DateTime
from sqlalchemy.sql import func
from core.database import Base


class DrawResult(Base):
    __tablename__ = "draw_results"

    id = Column(Integer, primary_key=True, index=True)
    game_type = Column(String(20), nullable=False, index=True)  # lotto649, super_lotto, daily_cash
    draw_term = Column(String(20), nullable=False, unique=True)
    draw_date = Column(Date, nullable=False)
    numbers = Column(ARRAY(Integer), nullable=False)
    special_number = Column(Integer, nullable=True)
    bonus_number = Column(Integer, nullable=True)
    source = Column(String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
