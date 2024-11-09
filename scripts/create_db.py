import sqlite3
import os

# Percorso del database
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "stargram.db")

def create_tables():
    """
    Crea il database e tutte le tabelle necessarie per l'applicazione.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Creazione della tabella Users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        instagram_id TEXT UNIQUE NOT NULL,
        username TEXT NOT NULL,
        profile_picture_url TEXT,
        follower_count INTEGER,
        following_count INTEGER,
        bio TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Creazione della tabella Posts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id TEXT UNIQUE NOT NULL,
        user_id INTEGER NOT NULL,
        image_url TEXT,
        caption TEXT,
        like_count INTEGER,
        comment_count INTEGER,
        created_time TIMESTAMP,
        engagement_score REAL,
        location_name TEXT,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );
    """)

    # Creazione della tabella Trends
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Trends (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        value TEXT NOT NULL,
        popularity_score INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Creazione della tabella HashtagRecommendations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS HashtagRecommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        hashtag TEXT NOT NULL,
        relevance_score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );
    """)

    # Creazione della tabella DescriptionRecommendations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DescriptionRecommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        sentiment TEXT,
        tone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );
    """)

    connection.commit()
    connection.close()
    print(f"Database creato con successo in {DB_PATH}")

if __name__ == "__main__":
    create_tables()
