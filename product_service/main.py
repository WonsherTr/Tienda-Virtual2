from fastapi import FastAPI
from routes import products
from db.database import engine
from models import product

product.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products.router)
