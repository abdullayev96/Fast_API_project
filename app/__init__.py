import os
from dotenv import load_dotenv
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()



app = FastAPI()


database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
debug_mode = os.getenv("DEBUG")



@app.get("/")
def read_root():
    return {
        "database_url": database_url,
        "secret_key": secret_key,
        "debug_mode": debug_mode
    }

