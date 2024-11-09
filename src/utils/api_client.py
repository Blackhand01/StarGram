import os
import requests
from dotenv import load_dotenv

# Carica le variabili di ambiente
load_dotenv()

def get_facebook_pages(access_token):
    url = "https://graph.facebook.com/v17.0/me/accounts"
    params = {"access_token": access_token}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise ValueError(f"Errore nel recupero delle pagine: {response.json()}")

    pages = response.json().get("data", [])
    if not pages:
        print("Nessuna pagina trovata.")
        return None

    for page in pages:
        print(f"Pagina: {page['name']}, ID: {page['id']}")
    return pages

ACCESS_TOKEN = os.getenv("TECHTWINS_ACCESS_TOKEN")

try:
    get_facebook_pages(ACCESS_TOKEN)
except Exception as e:
    print(f"Errore: {e}")
