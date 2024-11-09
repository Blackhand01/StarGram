import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_instagram_user_data(user_id):
    """
    Recupera i dati di un utente Instagram utilizzando l'API Graph.
    """
    api_key = os.getenv("INSTAGRAM_API_KEY")
    if not api_key:
        raise ValueError("Chiave INSTAGRAM_API_KEY non trovata! Verifica il file .env.")

    url = f"https://graph.instagram.com/{user_id}?fields=id,username,account_type,media_count&access_token={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Errore durante il recupero dei dati Instagram: {response.status_code}, {response.text}")
