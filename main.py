from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERVER_HELLO: str
    
settings = Settings()
app = FastAPI()

@app.get("/health-check")
def read_item():
    return {"Status": "ok"}

@app.get("/hello-world")
async def info():
    return {
        "text": settings.SERVER_HELLO,
    }