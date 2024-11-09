import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.api_client import fetch_instagram_user_data

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
    Punto di ingresso principale dell'applicazione.
    """
    try:
        load_dotenv()

        # Configura l'API Instagram
        configure_instagram_api()
        print("API Instagram configurata correttamente.")

        # Recupera i dati dell'utente
        user_id = os.getenv("INSTAGRAM_USER_ID")
        if not user_id:
            raise ValueError("ID utente Instagram non trovato! Verifica il file .env.")
        
        print(f"\nRecupero dati per l'utente Instagram con ID: {user_id}")
        user_data = fetch_instagram_user_data(user_id)
        print(f"Dati utente: {user_data}")

    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()
