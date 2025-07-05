from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from backend.utils.utils import hash_password
from passlib.context import CryptContext
from backend.models import UserAuth
from backend.auth.jwt_handler import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(UserAuth).filter(UserAuth.username == username).first()
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(data={"sub": username})
    return token


def create_user(user_data: dict, db: Session):
    """Creates a new user and stores it in the database."""
    try:
        existing_username = db.query(UserAuth).filter(UserAuth.username == user_data["username"]).first()

        if existing_username:
            raise HTTPException(status_code=400, detail="Username already taken")

        # Hash password and store in auth table
        hashed_password = hash_password(user_data["password"])
        new_auth = UserAuth(
            username=user_data["username"],
            password=hashed_password
        )
        db.add(new_auth)
        db.commit()
        db.refresh(new_auth)

        # 🔐 Generate JWT token for auto-login
        access_token = create_access_token(data={"sub": new_auth.username})

        # 🎯 Return token in response
        response = JSONResponse(
            status_code=201,
            content={
                "message": "User registered successfully",
                "access_token": access_token,
                "token-type": "Bearer-Token"
            }
        )
        response.headers["Authorization"] = f"Bearer {access_token}"

        return response

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create user: {str(e)}")