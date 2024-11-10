import os
import requests
from requests.exceptions import RequestException
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


def validate_access_token(access_token):
    """
    Verifica la validità del token di accesso tramite l'endpoint di debug di Facebook.
    """
    debug_url = "https://graph.facebook.com/debug_token"
    params = {
        "input_token": access_token,
        "access_token": access_token,  # Usa un token valido della tua app
    }
    print("\n=== Validazione del token di accesso ===")
    print(f"Endpoint: {debug_url}")
    print(f"Parametri: {params}")

    try:
        response = requests.get(debug_url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", {})
            print(f"Risultati debug token: {data}")
            
            if data.get("is_valid"):
                print("Token valido.")
                print(f"Permessi associati: {data.get('scopes', 'Nessun permesso trovato.')}")
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


def fetch_hashtag_id(hashtag_name):
    """
    Recupera l'ID di un hashtag di Instagram utilizzando l'API Graph.
    """
    # Carica il token d'accesso e l'ID utente dal file .env
    access_token = os.getenv("TECHTWINS_ACCESS_TOKEN")
    user_id = os.getenv("INSTAGRAM_USER_ID")
    
    if not access_token:
        raise ValueError("Token di accesso non configurato. Verifica il file .env.")
    if not user_id:
        raise ValueError("User ID di Instagram non configurato. Verifica il file .env.")
    
    # URL e parametri della richiesta
    api_url = "https://graph.facebook.com/v21.0/ig_hashtag_search"
    params = {
        "user_id": user_id,
        "q": hashtag_name, 
        "access_token": access_token,
    }

    print("\n=== Recupero ID Hashtag ===")
    print(f"Chiamata API URL: {api_url}")
    print(f"Parametri: {params}")
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        # Estrai i dati JSON
        data = response.json().get("data", [])
        if not data:
            print(f"Nessun ID trovato per l'hashtag '{hashtag_name}'.")
            return None
        
        # Restituisce il primo ID trovato
        return data[0]["id"]
    except requests.exceptions.HTTPError as http_err:
        print(f"\nErrore HTTP: {http_err}. Risposta: {response.text}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Errore di richiesta: {req_err}")
        return None
    except Exception as e:
        print(f"Errore sconosciuto: {e}")
        return None


def fetch_posts_for_hashtag(hashtag_id):
    """
    Recupera i contenuti multimediali relativi a un hashtag specifico.
    """
    access_token = os.getenv("INSTAGRAM_API_KEY")
    if not access_token:
        raise ValueError("Token di accesso non configurato. Verifica il file .env.")

    api_url = f"https://graph.facebook.com/v15.0/{hashtag_id}/top_media"
    params = {
        "user_id": os.getenv("INSTAGRAM_USER_ID"),
        "fields": "id,media_type,like_count,comments_count",
        "access_token": access_token,
    }

    print("\n=== Recupero Post Hashtag ===")
    print(f"Chiamata API URL: {api_url}")
    print(f"Parametri: {params}")

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json().get("data", [])
    except RequestException as e:
        print(f"Errore nel recupero dei contenuti multimediali per l'hashtag '{hashtag_id}': {e}")
        return []


