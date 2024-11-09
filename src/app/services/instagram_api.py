import os
import requests
from dotenv import load_dotenv

load_dotenv()

def configure_instagram_api():
    """
    Configura l'API Instagram utilizzando la chiave nel file .env.
    """
    api_key = os.getenv("INSTAGRAM_API_KEY")
    if not api_key:
        raise ValueError("Chiave INSTAGRAM_API_KEY non trovata!")
    return api_key


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


def fetch_hashtag_id(theme):
    """
    Recupera l'ID di un hashtag utilizzando il nome del tema.
    """
    access_token = configure_instagram_api()
    print("access_token",access_token)
    if not validate_access_token(access_token):
        print("Errore: Token di accesso non valido.")
        return None

    api_url = "https://graph.facebook.com/v15.0/ig_hashtag_search"
    params = {
        "user_id": os.getenv("INSTAGRAM_USER_ID"),
        "q": theme,
        "access_token": access_token,
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json().get("data", [])
        return data[0]["id"] if data else None
    except requests.exceptions.RequestException as e:
        print(f"Errore nel recupero dell'ID hashtag: {e}")
        return None



def fetch_posts_for_hashtag(hashtag_id):
    """
    Recupera i contenuti multimediali relativi a un hashtag specifico.
    """
    access_token = configure_instagram_api()
    api_url = f"https://graph.facebook.com/v15.0/{hashtag_id}/top_media"
    params = {
        "user_id": "8360743184034347",  # Sostituisci con un ID utente Instagram valido
        "fields": "id,media_type,like_count,comments_count",
        "access_token": access_token,
    }
    try:
        response = requests.get(api_url, params=params)
        return response.json().get("data", []) if response.status_code == 200 else []
    except Exception as e:
        print(f"Errore nel recupero dei contenuti multimediali: {e}")
        return []


def validate_access_token(access_token):
    """
    Verifica la validità del token di accesso tramite l'endpoint di debug di Facebook.
    """
    debug_url = f"https://graph.facebook.com/debug_token"
    params = {
        "input_token": access_token,
        "access_token": access_token,  # Usa un token valido della tua app
    }
    try:
        response = requests.get(debug_url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", {})
            if data.get("is_valid"):
                print("Token valido.")
                return True
            else:
                print(f"Token non valido: {data}")
                return False
        else:
            print(f"Errore durante la verifica del token: {response.status_code}, {response.text}")
            return False
    except Exception as e:
        print(f"Errore durante la validazione del token: {e}")
        return False
