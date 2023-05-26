from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import posts, users, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=[],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

@app.get("/")
def root():
    return {"message": "synced with current dir"}

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)