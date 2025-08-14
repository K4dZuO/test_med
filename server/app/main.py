from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import api


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000"],       # или ["*"] на время отладки
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.router)
