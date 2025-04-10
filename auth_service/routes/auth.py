from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: UserLogin):
    if user.username == "admin" and user.password == "admin123":
        return {"access_token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")
