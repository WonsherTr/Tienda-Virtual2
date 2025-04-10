from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.product import Product
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    iva: float
    size: str
    weight: str
    image_url: str
    category_id: int | None = None

@router.post("/")
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductBase])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
