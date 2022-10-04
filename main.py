from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
    
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
from api.fetch_price import DataFetcher

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
fetch_data = DataFetcher()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/read_bitcoin", response_model=List[schemas.Bitcoin])
async def read_bitcoin(skip: int = 1, limit: int = 365, db: Session = Depends(get_db)):
    bitcoins = crud.get_bitcoins(db, skip=skip, limit=limit)
    return bitcoins

@app.get("/fetch_bitcoin")
async def read_bitcoin():
    bitcoin_price = fetch_data.fetch_bitcoin_price()
    return bitcoin_price

@app.get("/read_ethareum")
async def read_ethareum():
    return {"ethareum": "Now Developing"}


@app.get("/fetch_ethareum")
async def read_ethareum():
    return {"ethareum": "Now Developing"}