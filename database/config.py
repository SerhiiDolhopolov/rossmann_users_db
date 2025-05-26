import os
from dotenv import load_dotenv

load_dotenv()

USERS_DB_USER = os.getenv("USERS_DB_USER")
USERS_DB_PASSWORD = os.getenv("USERS_DB_PASSWORD")
USERS_DB_HOST = os.getenv("USERS_DB_HOST")
USERS_DB_PORT = os.getenv("USERS_DB_PORT")
USERS_DB_DB = os.getenv("USERS_DB_DB")
