import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests
from PIL import Image

load_dotenv()

# Configura l'API Gemini
def configure_gemini_api():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Chiave GEMINI_API_KEY non trovata!")
    genai.configure(api_key=api_key)

# Analizza l'immagine per estrarre temi
def analyze_image_with_gemini(image_path):
    """
    Analizza un'immagine utilizzando Gemini e restituisce tre hashtag suggeriti.
    """
    number = 4
    configure_gemini_api()
    try:
        # Carica l'immagine con PIL
        image = Image.open(image_path)
        # Prompt per estrarre hashtag
        prompt = (
            f"Analyze the following image and provide up to {number} relevant hashtags. "
            "Base the hashtags on the prominent themes, objects, or concepts visible in the image. "
            "Each hashtag should be concise, meaningful, and reflective of the image's content."
        )

        JsonSchema = (
            """
            Return the hashtags as a valid JSON list in this format:
            ["hashtag1", "hashtag2", "hashtag3"]
            Ensure no additional text, symbols, or formatting around the list.
            """
        )

    
        # Usa il modello per generare contenuti basati sull'immagine
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content([prompt+JsonSchema, image])

        # Analizza la risposta
        if response and hasattr(response, "text"):
            hashtags = [tag.strip() for tag in response.text.split(",")]
            #print(f"hashtags: {hashtags[:number]}")
            return hashtags  # Restituisce solo i primi tre hashtag
        else:
            print("Risposta vuota o non valida dal modello.")
            return []
    except Exception as e:
        print(f"Errore durante l'analisi dell'immagine: {e}")
        return []



def fetch_hashtag_id(theme):
    """
    Recupera l'ID di un hashtag utilizzando il nome del tema.
    """
    access_token = os.getenv("INSTAGRAM_API_KEY")
    if not access_token:
        raise ValueError("Chiave INSTAGRAM_API_KEY non trovata!")

    api_url = "https://graph.facebook.com/v15.0/ig_hashtag_search"
    params = {
        "user_id": "8360743184034347",  # Sostituisci con l'ID utente Instagram valido
        "q": theme,
        "access_token": access_token,
    }

    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", [])
            if data:
                return data[0]["id"]
            else:
                print(f"Nessun ID trovato per il tema: {theme}")
                return None
        else:
            print(f"Errore nell'API Instagram: {response.status_code}, {response.json()}")
            return None
    except Exception as e:
        print(f"Errore nel recupero dell'ID hashtag: {e}")
        return None


def fetch_posts_for_hashtag(hashtag_id):
    """
    Recupera i contenuti multimediali relativi a un hashtag specifico.
    """
    access_token = os.getenv("INSTAGRAM_API_KEY")
    if not access_token:
        raise ValueError("Chiave INSTAGRAM_API_KEY non trovata!")

    api_url = f"https://graph.facebook.com/v15.0/{hashtag_id}/top_media"
    params = {
        "user_id": "8360743184034347",  # Sostituisci con l'ID utente Instagram valido
        "fields": "id,media_type,like_count,comments_count",
        "access_token": access_token,
    }

    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(f"Errore nell'API Instagram: {response.status_code}, {response.json()}")
            return []
    except Exception as e:
        print(f"Errore nel recupero dei contenuti multimediali: {e}")
        return []


def calculate_weighted_interaction(posts):
    """
    Calcola la media pesata delle interazioni (like, commenti, ecc.) per i post.
    """
    try:
        if not posts:
            print("Nessun post fornito per il calcolo.")
            return 0

        total_interactions = 0
        total_weights = 0

        for post in posts:
            likes = post.get("like_count", 0)
            comments = post.get("comments_count", 0)
            # Pesi: assegniamo più peso ai like rispetto ai commenti
            interaction_score = likes * 0.7 + comments * 0.3
            total_interactions += interaction_score
            total_weights += 1

        weighted_average = total_interactions / total_weights if total_weights > 0 else 0
        return round(weighted_average, 2)
    except Exception as e:
        print(f"Errore nel calcolo delle interazioni pesate: {e}")
        return 0
