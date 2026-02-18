import os 
from dotenv import load_dotenv



load_dotenv();

APP_NAME = os.getenv("APP_NAME","Default App Name");
LOG_LEVEL = os.getenv("LOG_LEVEL","INFO").upper();
DEBUG = os.getenv("DEBUG","true") == "true";
