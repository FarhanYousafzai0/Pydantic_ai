from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.logger import logger

router = APIRouter()

class User(BaseModel):
    name: str
    age: int

@router.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "API is running"}

@router.post("/user")
def create_user(user: User):
    logger.debug(f"Received user object: {user}")

    logger.info(f"Creating user: {user.name} with age {user.age}")

    if user.age < 0:
        logger.warning("Negative age detected")
        raise HTTPException(status_code=400, detail="Age cannot be negative")

    result = {
        "message": f"User {user.name} created successfully",
        "age_in_5_years": user.age + 5
    }

    logger.debug(f"Result: {result}")
    return result
