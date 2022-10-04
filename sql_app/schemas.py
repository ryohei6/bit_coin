from pydantic import BaseModel

class Bitcoin(BaseModel):
    date: str
    price: int
    
    class Config:
        orm_mode = True
    
class Ethareum(BaseModel):
    date: str
    price: int
    
    class Config:
        orm_mode = True