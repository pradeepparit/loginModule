from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.auth.controller import authenticate_user
from backend.auth import controller

router = APIRouter()

@router.post("/login")
def login_user(payload: dict, response: Response, db: Session = Depends(get_db)):

    token = authenticate_user(payload, db)

    isAuthorised = True if token else False

    if isAuthorised:
        response.headers["Authorization"] = f"Bearer {token}"
    return {"message": "Login successful", "isAuthorised": isAuthorised, "token": token, "token-type": "Bearer-Token"}

@router.post("/user_registration/")
def register_user(user_data: dict, db: Session = Depends(get_db)):
    return controller.register_user(user_data, db)
