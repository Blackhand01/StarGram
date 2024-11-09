import os
from dotenv import load_dotenv
from app.services.gemini_api import configure_gemini_api
from app.services.instagram_api import configure_instagram_api, fetch_instagram_user_data
from app.services.hashtag_recommendation import suggest_hashtags_and_calculate_engagement


def main():
    """
    Punto di ingresso principale per configurare le API e gestire il processo di analisi.
    """
    # Carica le variabili di ambiente
    load_dotenv()

    # Recupera l'ID utente Instagram
    user_id = os.getenv("INSTAGRAM_USER_ID")
    if not user_id:
        print("Errore: ID utente Instagram non configurato.")
        return

    # # Configura le API
    # try:
    #     configure_gemini_api()
    #     print("API GEMINI configurata correttamente.")
    #     configure_instagram_api()
    #     print("API Instagram configurata correttamente.")

    #     user_data = fetch_instagram_user_data(user_id)
    #     print(f"Dati utente: {user_data}")

    # except ValueError as e:
    #     print(f"Errore nella configurazione delle API: {e}")
    #     return

    # Percorso dell'immagine da analizzare
    image_path = "data/prova.jpeg"

   
    # Avvia il processo di suggerimento hashtag e calcolo dell'engagement
    suggest_hashtags_and_calculate_engagement(image_path, user_id)

