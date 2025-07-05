from fastapi import HTTPException

def checkEmptyField(value: str, fieldName):
    """Ensure filed is not empty."""
    if not value.strip():
        raise HTTPException(status_code=400, detail=f"{fieldName} cannot be empty.")
    return value

def cannotEmpty(value, field_name="Value"):
    if not value.strip():
        raise HTTPException(status_code=400, detail=f"{field_name} cannot be empty")

def register_user(user_data: dict):
    validate_username(user_data["username"])
    validate_password(user_data["password"])

def validate_username(username: str):
    """Ensure username is not empty."""
    return cannotEmpty(username, 'username')

def validate_password(password: str):
    """Ensure password is not empty (hashing happens later)."""
    return cannotEmpty(password, 'password')