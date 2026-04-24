from fastapi import FastAPI

app = FastAPI(
    title="Game Collection API",
    description="REST API for managing a personal video game collection",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Game Collection API",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}