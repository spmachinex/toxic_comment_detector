from fastapi import FastAPI
from .routers import comments

app = FastAPI()
app.include_router(comments.router)