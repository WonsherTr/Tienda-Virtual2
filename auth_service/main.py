from fastapi import FastAPI
from auth_service.routes import auth

app = FastAPI()

app.include_router(auth.router)
