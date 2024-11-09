import os
import sys
from unittest.mock import patch, MagicMock
import pytest

# Aggiungi il percorso della directory src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.api_client import fetch_instagram_user_data

@patch("requests.get")
def test_fetch_instagram_user_data(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": "1234567890",
        "username": "test_user",
        "account_type": "BUSINESS",
        "media_count": 42
    }
    mock_get.return_value = mock_response

    user_id = "1234567890"
    result = fetch_instagram_user_data(user_id)
    assert result["username"] == "test_user"
    assert result["account_type"] == "BUSINESS"
    assert result["media_count"] == 42
