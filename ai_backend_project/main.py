







from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from logging.handlers import RotatingFileHandler
import logging
from dotenv import load_dotenv
import os


# Log Dotenv File :

load_dotenv();

APP_NAME = os.getenv("APP_NAME","Default App Name");
LOG_LEVEL = os.getenv("LOG_LEVEL","INFO").upper();
DEBUG = os.getenv("DEBUG","true") == "true";


os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("app_logger")
logger.setLevel(getattr(logging,LOG_LEVEL,logging.INFO))

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=1_000_000,
    backupCount=3
)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



app = FastAPI();

class User(BaseModel):
    name:str
    age:int



@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {
        "app": APP_NAME,
        "debug": DEBUG,
        "message": "API is running"
    }

    





@app.post("/user")

def create_user(user:User):
    try:
        logger.debug(f"Received raw user data: {user.model_dump_json()}")
        logger.info(f"Creating user: {user.name} with age {user.age}")

        if user.age < 0:
            logger.warning(f"Age cannot be negative for user: {user.name}")
            raise HTTPException(status_code=400, detail="Age cannot be negative")


        result = {
            "message":f"User {user.name} created successfully",
            "age_in_5_years":user.age + 5
        }
        logger.debug(f"Returning result: {result}")
        logger.info(f"User {user.name} created successfully")
        return result

    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail=str(e))

