import os
import pytest
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import list_models, generate_content

# Test per verificare la configurazione dell'API
def test_api_key_load():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    assert api_key is not None, "Chiave API non trovata! Verifica il file .env."

# Test con mocking per evitare richieste reali
@patch("google.generativeai.list_models")
def test_list_models(mock_list_models):
    mock_list_models.return_value = [
        {"name": "gemini-1.5-flash", "display_name": "Gemini 1.5 Flash"}
    ]
    models = list_models()
    assert len(models) == 1
    assert models[0]["name"] == "gemini-1.5-flash"

@patch("google.generativeai.GenerativeModel")
def test_generate_content(mock_generative_model):
    mock_instance = MagicMock()
    mock_instance.generate_content.return_value = MagicMock(text="Benvenuto in Italia!")
    mock_generative_model.return_value = mock_instance
    
    prompt = "Suggerisci una caption per un post Instagram su viaggi in Italia."
    model_name = "gemini-1.5-flash"
    result = generate_content(prompt, model_name)
    
    assert result == "Benvenuto in Italia!", "Il contenuto generato non è corretto!"
