import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.api_client import fetch_instagram_user_data, fetch_instagram_user_posts
from app.services.hashtag_recommendation import (
    analyze_image_with_gemini,
    fetch_hashtag_id,
    fetch_posts_for_hashtag,
    calculate_weighted_interaction,
)
import re
import json
import ast

def configure_gemini_api():
    """
    Configura l'API GEMINI utilizzando la chiave dal file .env.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Chiave GEMINI_API_KEY non trovata! Assicurati che .env contenga GEMINI_API_KEY.")
    genai.configure(api_key=api_key)

def configure_instagram_api():
    """
    Configura l'API Instagram utilizzando la chiave dal file .env.
    """
    api_key = os.getenv("INSTAGRAM_API_KEY")
    if not api_key:
        raise ValueError("Chiave INSTAGRAM_API_KEY non trovata! Assicurati che .env contenga INSTAGRAM_API_KEY.")
    # Simulazione di configurazione per Instagram API (sostituire con libreria Instagram se necessaria)
    return api_key

def list_models():
    """
    Restituisce la lista dei modelli disponibili da GEMINI.
    """
    return genai.list_models()

def generate_content(prompt, model_name):
    """
    Genera contenuto utilizzando un modello specifico GEMINI.
    """
    model = genai.GenerativeModel(model_name=model_name)
    response = model.generate_content(prompt)
    if not response or not response.text:
        raise ValueError("La generazione del contenuto è fallita!")
    return response.text

def suggest_hashtags_for_post(image_path, location):
    """
    Suggerisce hashtag per un nuovo post.
    """
    print("\n1. Analisi dell'immagine con Gemini...")
    themes = analyze_image_with_gemini(image_path)
    if themes:
        print(f"Temi rilevati dall'immagine:")
        for theme in themes:
            print(f"- {theme}")
    else:
        print("Nessun tema rilevato dall'immagine.")

    print("\n2. Recupero degli hashtag in tendenza...")
    hashtags = fetch_trending_hashtags(themes, location)
    if hashtags:
        print("\nHashtag consigliati:")
        for hashtag in hashtags:
            print(f"- {hashtag}")
    else:
        print("Nessun hashtag trovato.")




# Funzione per normalizzare gli hashtag suggeriti

def normalize_suggested_hashtags(suggested_hashtags):
    try:
        # Unire la lista in una stringa
        raw_string = ''.join(suggested_hashtags)
        
        # Rimuovere caratteri non validi e aggiustare la formattazione
        raw_string = raw_string.replace("'", '"').strip()
        
        # Individuare solo il contenuto tra le parentesi quadre
        if raw_string.startswith('["') and raw_string.endswith('"]'):
            # Pulire i caratteri iniziali e finali
            clean_string = raw_string.strip('[]')
            # Suddividere gli elementi tra virgole, garantendo la pulizia
            hashtags = [tag.strip('"') for tag in clean_string.split('", "')]
        else:
            raise ValueError("Formato degli hashtag non riconosciuto.")
        
        return hashtags
    except Exception as e:
        print(f"Errore durante la normalizzazione degli hashtag: {e}")
        return []





def main():

    # try:
    #     load_dotenv()

    #     # Configurazione API GEMINI
    #     configure_gemini_api()
    #     print("API GEMINI configurata correttamente.")

        # Elenca i modelli GEMINI disponibili
        # print("\nModelli GEMINI disponibili:")
        # models = list_models()
        # for model in models:
        #     print(f"- {model.display_name} (ID: {model.name})")

        # # Esempio di utilizzo GEMINI: generazione di testo
        # print("\nGenerazione di contenuto con GEMINI:")
        # prompt = "Suggerisci una caption per un post Instagram su viaggi in Italia."
        # model_name = "gemini-1.5-flash"
        # result = generate_content(prompt, model_name)
        # print(f"Prompt: {prompt}")
        # print(f"Risultato: {result}")

        # Configurazione API Instagram
    """
    Punto di ingresso principale per analizzare un'immagine e suggerire hashtag.
    """
    try:
        image_path = "data/prova.jpeg"  # Percorso dell'immagine da analizzare
        print("1. Analisi dell'immagine con Gemini...")
        suggested_hashtags = analyze_image_with_gemini(image_path)
        print(f"Hashtag suggeriti dall'immagine: {suggested_hashtags}")

        if not suggested_hashtags:
            print("Nessun hashtag suggerito.")
            return
        # Normalizza gli hashtag suggeriti
        clean_suggested_hashtags = normalize_suggested_hashtags(suggested_hashtags)
        print(f"Hashtag normalizzati: {clean_suggested_hashtags}")

        # Se non ci sono hashtag validi, termina l'elaborazione
        if not clean_suggested_hashtags:
            print("Nessun hashtag suggerito valido.")
            return

        # print("\n2. Recupero degli hashtag in tendenza...")
        # all_posts = []
        # for theme in suggested_hashtags:
        #     hashtag_id = fetch_hashtag_id(theme)
        #     if hashtag_id:
        #         posts = fetch_posts_for_hashtag(hashtag_id)
        #         all_posts.extend(posts)

        # if not all_posts:
        #     print("Nessun post trovato per gli hashtag suggeriti.")
        #     return

        # print("\n3. Calcolo della media pesata delle interazioni...")
        # weighted_score = calculate_weighted_interaction(all_posts)
        # print(f"Media pesata delle interazioni: {weighted_score}")

    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()