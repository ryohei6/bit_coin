from sqlalchemy.orm import Session
from . import models

# bitcoinデータ取得
def get_bitcoins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bitcoin).offset(skip).limit(limit).all()

# ethareumデータ取得
def get_ethareums(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ethareum).offset(skip).limit(limit).all()