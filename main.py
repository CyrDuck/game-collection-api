from fastapi import FastAPI
from database import Base, engine
from routers import games

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Game Collection API",
    description="REST API for managing a personal video game collection",
    version="0.2.0"
)

app.include_router(games.router)


@app.get("/")
def root():
    return {
        "message": "Game Collection API",
        "version": "0.2.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}