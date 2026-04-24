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

from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from models import Game


@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Game).count()
    completed = db.query(Game).filter(Game.status == "completed").count()
    playing = db.query(Game).filter(Game.status == "playing").count()
    wishlist = db.query(Game).filter(Game.status == "wishlist").count()
    return {
        "total_games": total,
        "completed": completed,
        "playing": playing,
        "wishlist": wishlist
    }