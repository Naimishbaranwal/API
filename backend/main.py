from fastapi import FastAPI
import emoji
from core.config import settings
# print(emoji.emojize("Python is :rocket:"))




app=FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

@app.get("/")
def hello():
    return {"msg":"Hello FastAPI 🚀"}