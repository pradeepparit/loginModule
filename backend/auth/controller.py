from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from backend.auth.service import authenticate_user as authenticate_user_service
from backend.auth.service import create_user
from backend.auth import eval as eval

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(payload: dict, db: Session):

    eval.checkEmptyField(payload['username'], 'username')
    eval.checkEmptyField(payload['password'], 'password')

    return authenticate_user_service(payload['username'], payload['password'], db)


def register_user(user_data: dict, db: Session):
    """Validates and creates a new user."""
    try:
        # Validate input fields
        eval.register_user(user_data)

        # Pass validated data to service
        return create_user(user_data, db)

    except HTTPException as e:
        raise e  # Pass FastAPI errors as they are
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")