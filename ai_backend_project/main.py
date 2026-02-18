from fastapi import FastAPI
from pydantic import BaseModel
import logging 



logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


logger = logging.getLogger(__name__)
app = FastAPI()




class User(BaseModel):
    name:str
    age:int

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "API is running"}



@app.post("/user")
def create_user(user:User):

    logger.info(f"Creating user {user.name} with age {user.age}")
    result = {
        "message":f"User {user.name} created successfully",
        "age_in_5_years":f"User age will be in next 5 years will be {user.age + 5}"
    }

    logger.info(f"User {user.name} created successfully")
    return result




