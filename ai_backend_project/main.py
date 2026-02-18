from fastapi import FastAPI
from app.routes import router
from app.config import APP_NAME, DEBUG


app = FastAPI(title=APP_NAME,debug=DEBUG)

app.include_router(router);