from database import SessionLocal, engine
from models import Base, Game

Base.metadata.create_all(bind=engine)

sample_games = [
    {"title": "Elden Ring", "platform": "PC", "genre": "RPG", "release_year": 2022, "status": "completed", "rating": 9.5, "notes": "Masterpiece open world RPG"},
    {"title": "Cyberpunk 2077", "platform": "PC", "genre": "Action RPG", "release_year": 2020, "status": "playing", "rating": 8.0, "notes": "Great after patches"},
    {"title": "Hollow Knight", "platform": "PC", "genre": "Metroidvania", "release_year": 2017, "status": "completed", "rating": 9.0, "notes": "Challenging but rewarding"},
    {"title": "Hades", "platform": "PC", "genre": "Roguelike", "release_year": 2020, "status": "completed", "rating": 9.3, "notes": "Best roguelike ever made"},
    {"title": "God of War", "platform": "PS5", "genre": "Action Adventure", "release_year": 2018, "status": "completed", "rating": 9.8, "notes": "Perfect game"},
    {"title": "Celeste", "platform": "PC", "genre": "Platformer", "release_year": 2018, "status": "completed", "rating": 8.8, "notes": "Incredible platformer with great story"},
    {"title": "Stardew Valley", "platform": "PC", "genre": "Simulation", "release_year": 2016, "status": "playing", "rating": 8.5, "notes": "Relaxing farming game"},
    {"title": "Dark Souls 3", "platform": "PC", "genre": "RPG", "release_year": 2016, "status": "dropped", "rating": 7.5, "notes": "Too difficult for me"},
    {"title": "The Witcher 3", "platform": "PC", "genre": "RPG", "release_year": 2015, "status": "completed", "rating": 9.7, "notes": "Best RPG ever made"},
    {"title": "Minecraft", "platform": "PC", "genre": "Sandbox", "release_year": 2011, "status": "playing", "rating": 9.0, "notes": "Timeless classic"},
    {"title": "Sekiro", "platform": "PC", "genre": "Action RPG", "release_year": 2019, "status": "wishlist", "rating": None, "notes": "Want to try after Elden Ring"},
    {"title": "Disco Elysium", "platform": "PC", "genre": "RPG", "release_year": 2019, "status": "wishlist", "rating": None, "notes": "Highly recommended by friends"},
    {"title": "Red Dead Redemption 2", "platform": "PS5", "genre": "Action Adventure", "release_year": 2018, "status": "completed", "rating": 9.6, "notes": "Best story in gaming"},
    {"title": "Spider-Man 2", "platform": "PS5", "genre": "Action Adventure", "release_year": 2023, "status": "completed", "rating": 9.0, "notes": "Amazing web swinging"},
    {"title": "Horizon Forbidden West", "platform": "PS5", "genre": "Action RPG", "release_year": 2022, "status": "playing", "rating": 8.3, "notes": "Beautiful open world"},
    {"title": "The Last of Us Part I", "platform": "PS5", "genre": "Action Adventure", "release_year": 2022, "status": "completed", "rating": 9.4, "notes": "Emotional masterpiece"},
    {"title": "Demon Souls Remake", "platform": "PS5", "genre": "RPG", "release_year": 2020, "status": "dropped", "rating": 7.0, "notes": "Too punishing"},
    {"title": "Returnal", "platform": "PS5", "genre": "Roguelike", "release_year": 2021, "status": "wishlist", "rating": None, "notes": "Looks very interesting"},
    {"title": "Animal Crossing", "platform": "Switch", "genre": "Simulation", "release_year": 2020, "status": "completed", "rating": 8.2, "notes": "Perfect pandemic game"},
    {"title": "Breath of the Wild", "platform": "Switch", "genre": "Action Adventure", "release_year": 2017, "status": "completed", "rating": 9.5, "notes": "Redefined open world games"},
    {"title": "Tears of the Kingdom", "platform": "Switch", "genre": "Action Adventure", "release_year": 2023, "status": "playing", "rating": 9.4, "notes": "Even better than BOTW"},
    {"title": "Metroid Dread", "platform": "Switch", "genre": "Metroidvania", "release_year": 2021, "status": "completed", "rating": 8.7, "notes": "Best Metroid in years"},
    {"title": "Splatoon 3", "platform": "Switch", "genre": "Shooter", "release_year": 2022, "status": "playing", "rating": 8.0, "notes": "Fun multiplayer shooter"},
    {"title": "Fire Emblem Engage", "platform": "Switch", "genre": "Strategy RPG", "release_year": 2023, "status": "wishlist", "rating": None, "notes": "Looks great"},
    {"title": "Baldurs Gate 3", "platform": "PC", "genre": "RPG", "release_year": 2023, "status": "playing", "rating": 9.8, "notes": "Best RPG of the decade"},
    {"title": "Starfield", "platform": "PC", "genre": "Action RPG", "release_year": 2023, "status": "dropped", "rating": 6.5, "notes": "Disappointing after Skyrim"},
    {"title": "Diablo 4", "platform": "PC", "genre": "Action RPG", "release_year": 2023, "status": "completed", "rating": 7.8, "notes": "Fun but repetitive"},
    {"title": "Resident Evil 4 Remake", "platform": "PC", "genre": "Survival Horror", "release_year": 2023, "status": "completed", "rating": 9.3, "notes": "Perfect remake"},
    {"title": "Dead Space Remake", "platform": "PC", "genre": "Survival Horror", "release_year": 2023, "status": "completed", "rating": 9.0, "notes": "Terrifying and beautiful"},
    {"title": "Lies of P", "platform": "PC", "genre": "Action RPG", "release_year": 2023, "status": "completed", "rating": 8.5, "notes": "Surprisingly great Soulslike"},
    {"title": "Sea of Stars", "platform": "PC", "genre": "JRPG", "release_year": 2023, "status": "wishlist", "rating": None, "notes": "Beautiful pixel art RPG"},
    {"title": "Dave the Diver", "platform": "PC", "genre": "Adventure", "release_year": 2023, "status": "completed", "rating": 8.8, "notes": "Unique and charming"},
    {"title": "Forza Horizon 5", "platform": "Xbox", "genre": "Racing", "release_year": 2021, "status": "completed", "rating": 9.0, "notes": "Best racing game"},
    {"title": "Halo Infinite", "platform": "Xbox", "genre": "Shooter", "release_year": 2021, "status": "dropped", "rating": 7.0, "notes": "Disappointing campaign"},
    {"title": "Ori and the Will of the Wisps", "platform": "Xbox", "genre": "Platformer", "release_year": 2020, "status": "completed", "rating": 9.2, "notes": "Stunning visuals and music"},
    {"title": "Cuphead", "platform": "Xbox", "genre": "Platformer", "release_year": 2017, "status": "completed", "rating": 8.5, "notes": "Incredible art style"},
    {"title": "Among Us", "platform": "PC", "genre": "Party", "release_year": 2018, "status": "completed", "rating": 7.5, "notes": "Fun with friends"},
    {"title": "Fall Guys", "platform": "PC", "genre": "Party", "release_year": 2020, "status": "dropped", "rating": 7.0, "notes": "Gets boring quickly"},
    {"title": "It Takes Two", "platform": "PC", "genre": "Co-op Adventure", "release_year": 2021, "status": "completed", "rating": 9.5, "notes": "Best co-op game ever"},
    {"title": "Portal 2", "platform": "PC", "genre": "Puzzle", "release_year": 2011, "status": "completed", "rating": 9.8, "notes": "Perfect puzzle game"},
    {"title": "Outer Wilds", "platform": "PC", "genre": "Adventure", "release_year": 2019, "status": "completed", "rating": 9.6, "notes": "Most unique game ever made"},
    {"title": "Subnautica", "platform": "PC", "genre": "Survival", "release_year": 2018, "status": "completed", "rating": 9.0, "notes": "Terrifying underwater survival"},
    {"title": "Deep Rock Galactic", "platform": "PC", "genre": "Co-op Shooter", "release_year": 2020, "status": "playing", "rating": 9.1, "notes": "Rock and Stone"},
    {"title": "Monster Hunter Rise", "platform": "Switch", "genre": "Action RPG", "release_year": 2021, "status": "completed", "rating": 8.6, "notes": "Great entry point for series"},
    {"title": "Persona 5 Royal", "platform": "PC", "genre": "JRPG", "release_year": 2019, "status": "completed", "rating": 9.4, "notes": "Style and substance"},
    {"title": "Final Fantasy XVI", "platform": "PS5", "genre": "Action RPG", "release_year": 2023, "status": "completed", "rating": 8.2, "notes": "Great story weak gameplay"},
    {"title": "Armored Core VI", "platform": "PC", "genre": "Action", "release_year": 2023, "status": "wishlist", "rating": None, "notes": "FromSoftware mecha game"},
    {"title": "Vampire Survivors", "platform": "PC", "genre": "Roguelike", "release_year": 2022, "status": "completed", "rating": 8.9, "notes": "Addictive simple gameplay"},
    {"title": "Ghostwire Tokyo", "platform": "PC", "genre": "Action Adventure", "release_year": 2022, "status": "dropped", "rating": 6.8, "notes": "Beautiful but repetitive"},
    {"title": "Tunic", "platform": "PC", "genre": "Adventure", "release_year": 2022, "status": "wishlist", "rating": None, "notes": "Cute fox adventure game"},
]


def seed():
    db = SessionLocal()
    if db.query(Game).count() > 0:
        print("Database already has data, skipping seed.")
        db.close()
        return
    for g in sample_games:
        db.add(Game(**g))
    db.commit()
    db.close()
    print(f"Seeded {len(sample_games)} games successfully.")


if __name__ == "__main__":
    seed()