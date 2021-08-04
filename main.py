from fastapi import FastAPI
from core.config import Settings as S


app = FastAPI(title=S.PROJECT_TITLE,version=S.PROJECT_VERSION)

@app.get("/")
def hello_api():
    return {"detail" : "Hello, World!"}
