from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    iva = Column(Float, nullable=False)
    size = Column(String(50))
    weight = Column(String(50))
    image_url = Column(String(255))
    category_id = Column(Integer, nullable=True)
