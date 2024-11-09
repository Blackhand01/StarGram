import os
from dotenv import load_dotenv
import google.generativeai as genai

def configure_api():
    """
    Configura l'API utilizzando la chiave dal file .env.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:  # Verifica che la chiave API sia presente
        raise ValueError("Chiave API non trovata! Assicurati che .env contenga GEMINI_API_KEY.")
    genai.configure(api_key=api_key)


def list_models():
    """
    Restituisce la lista dei modelli disponibili.
    """
    return genai.list_models()

def generate_content(prompt, model_name):
    """
    Genera contenuto utilizzando un modello specifico.
    """
    model = genai.GenerativeModel(model_name=model_name)
    response = model.generate_content(prompt)
    if not response or not response.text:
        raise ValueError("La generazione del contenuto è fallita!")
    return response.text

def main():
    """
    Punto di ingresso principale dell'applicazione.
    """
    try:
        configure_api()
        print("API configurata correttamente.")
        
        # Elenca i modelli disponibili
        print("\nModelli disponibili:")
        models = list_models()
        for model in models:
            print(f"- {model.display_name} (ID: {model.name})")
        
        # Esempio di utilizzo: generazione di testo
        print("\nGenerazione di contenuto:")
        prompt = "Suggerisci una caption per un post Instagram su viaggi in Italia."
        model_name = "gemini-1.5-flash"
        result = generate_content(prompt, model_name)
        print(f"Prompt: {prompt}")
        print(f"Risultato: {result}")
    
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()
