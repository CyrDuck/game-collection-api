# Game Collection API

A RESTful API built with FastAPI and SQLite for managing a personal video game collection.
Developed as part of XJCO3011 Web Services and Web Data module at the University of Leeds.

## Features

- Full CRUD operations for game entries (Create, Read, Update, Delete)
- Filter games by platform and play status
- Title keyword search across the collection
- Collection statistics endpoint
- Genre and platform analytics
- 50 pre-loaded game entries across PC, PS5, Switch and Xbox
- Input validation with Pydantic v2
- Auto-generated interactive API documentation via Swagger UI

## Tech Stack

- **Framework**: FastAPI 0.115.0 (Python 3.13)
- **Database**: SQLite via SQLAlchemy ORM
- **Validation**: Pydantic v2
- **Server**: Uvicorn

## Project Structure

```
game-collection-api/
├── main.py           # App entry point, stats and analytics endpoints
├── database.py       # Database engine and session management
├── models.py         # SQLAlchemy Game model
├── schemas.py        # Pydantic request/response schemas
├── seed_data.py      # 50-entry sample dataset loader
├── routers/
│   ├── __init__.py
│   └── games.py      # CRUD and search route handlers
├── docs/
│   └── api_documentation.pdf
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/CyrDuck/game-collection-api.git
cd game-collection-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Load sample data (optional)

```bash
python seed_data.py
```

### 6. Access the API

- **Swagger UI**: http://127.0.0.1:8000/docs
- **Base URL**: http://127.0.0.1:8000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info and version |
| GET | `/health` | Server health check |
| GET | `/stats` | Collection statistics (total, by status) |
| GET | `/stats/genres` | Game count grouped by genre |
| GET | `/stats/platforms` | Game count grouped by platform |
| POST | `/games/` | Add a new game to the collection |
| GET | `/games/` | List all games (supports filtering) |
| GET | `/games/{id}` | Get a specific game by ID |
| PUT | `/games/{id}` | Update a game entry |
| DELETE | `/games/{id}` | Delete a game entry |
| GET | `/games/search/title` | Search games by title keyword |

## Game Status Values

| Status | Meaning |
|--------|---------|
| `wishlist` | Games you want to play |
| `playing` | Currently playing |
| `completed` | Finished |
| `dropped` | Stopped playing |

## Example Request

```bash
# Add a new game
curl -X POST http://127.0.0.1:8000/games/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Elden Ring",
    "platform": "PC",
    "genre": "RPG",
    "release_year": 2022,
    "status": "completed",
    "rating": 9.5,
    "notes": "Masterpiece open world RPG"
  }'

# Filter games by platform and status
GET http://127.0.0.1:8000/games/?platform=PC&status=completed

# Search by title
GET http://127.0.0.1:8000/games/search/title?q=ring
```

## API Documentation

Full API documentation including all endpoints, parameters, request/response examples and error codes:

[docs/api_documentation.pdf](docs/api_documentation.pdf)

## Technical Report

See `technical_report.pdf` submitted via Minerva for full design justification, architecture decisions, testing approach, and Generative AI declaration.
