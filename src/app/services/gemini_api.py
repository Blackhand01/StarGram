import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

def configure_gemini_api():
    """
    Configura l'API Gemini utilizzando la chiave nel file .env.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Chiave GEMINI_API_KEY non trovata!")
    genai.configure(api_key=api_key)


def analyze_image(image_path, number=4):
    """
    Analizza un'immagine con l'API Gemini e restituisce fino a `number` hashtag rilevanti.
    """
    configure_gemini_api()
    try:
        image = Image.open(image_path)
        prompt = (
            f"Analyze the following image and provide up to {number} relevant hashtags. "
            "Base the hashtags on the prominent themes, objects, or concepts visible in the image. "
            "Each hashtag should be concise, meaningful, and reflective of the image's content."
        )
        json_schema = """
        The hashtags must be returned as a valid JSON array with no additional text or formatting, e.g.:
        ["hashtag1", "hashtag2", "hashtag3"]
        Ensure proper JSON syntax.
        """
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content([prompt + json_schema, image])

        if response and hasattr(response, "text"):
            # Verifica che il risultato sia un JSON valido
            import json
            try:
                hashtags = json.loads(response.text)
                return hashtags[:number]  # Restituisce solo i primi `number` hashtag
            except json.JSONDecodeError:
                print("Risposta JSON non valida ricevuta dal modello.")
                return []
        else:
            print("Risposta vuota o non valida dal modello.")
            return []
    except Exception as e:
        print(f"Errore durante l'analisi dell'immagine: {e}")
        return []
