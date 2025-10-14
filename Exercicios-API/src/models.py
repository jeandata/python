from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from db import Base

class Cotacao(Base):
    __tablename__ = 'cotacao'
    id = Column(Integer, primary_key=True, index=True)
    criptomoeda = Column(String(50), nullable = False)
    moeda = Column(String(20))
    valor = Column(Float)
    created_at = Column(DateTime, default=func.now())
