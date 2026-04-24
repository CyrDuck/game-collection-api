from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import Base, engine, get_db
from models import Game
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


@app.get("/stats/genres")
def get_genre_stats(db: Session = Depends(get_db)):
    data = db.query(Game.genre, func.count(Game.id)).group_by(Game.genre).all()
    return {"genres": [{"genre": g, "count": c} for g, c in data]}


@app.get("/stats/platforms")
def get_platform_stats(db: Session = Depends(get_db)):
    data = db.query(Game.platform, func.count(Game.id)).group_by(Game.platform).all()
    return {"platforms": [{"platform": p, "count": c} for p, c in data]}