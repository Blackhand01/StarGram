import os
import sys
from unittest.mock import patch, MagicMock
import pytest

# Aggiungi il percorso della directory src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.api_client import fetch_instagram_user_data, fetch_instagram_user_posts


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

@patch("utils.api_client.requests.get")
def test_fetch_instagram_user_posts(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "data": [
            {
                "id": "123456",
                "caption": "Un bellissimo tramonto!",
                "media_type": "IMAGE",
                "media_url": "https://example.com/photo.jpg",
                "timestamp": "2024-11-08T10:00:00Z"
            }
        ]
    }
    
    user_id = "123456789"
    posts = fetch_instagram_user_posts(user_id)
    assert len(posts) == 1
    assert posts[0]["id"] == "123456"
    assert posts[0]["media_type"] == "IMAGE"
    assert posts[0]["media_url"] == "https://example.com/photo.jpg"
    assert posts[0]["timestamp"] == "2024-11-08T10:00:00Z"


@patch("requests.get")
def test_fetch_trending_hashtags(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "data": [
            {"id": "17843876082292306", "name": "#travel"},
            {"id": "17843876082292307", "name": "#adventure"}
        ]
    }

    themes = ["travel", "adventure"]
    location = "Italy"
    hashtags = fetch_trending_hashtags(themes, location)

    assert len(hashtags) == 2
    assert hashtags[0]["name"] == "#travel"
    assert hashtags[1]["name"] == "#adventure"
