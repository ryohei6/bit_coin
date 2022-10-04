from sqlalchemy import Column, String, Integer
from .database import Base

class Bitcoin(Base):
    __tablename__ = 'bitcoin'
    date = Column(String, nullable=False, primary_key=True)
    price = Column(Integer, index=True)
    
class Ethareum(Base):
    __tablename__ = 'ethareum'
    date = Column(String, nullable=False, primary_key=True)
    price = Column(Integer, index=True)