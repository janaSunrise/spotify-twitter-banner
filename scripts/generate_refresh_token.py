import base64
from typing import Any, Dict, cast

import requests
from decouple import config

from app.utils import generate_oauth_url


class Config:
    SPOTIFY_CLIENT_ID = cast(str, config("SPOTIFY_CLIENT_ID"))
    SPOTIFY_CLIENT_SECRET = cast(str, config("SPOTIFY_CLIENT_SECRET"))
    SPOTIFY_REDIRECT_URI = cast(str, config("SPOTIFY_REDIRECT_URI", default="http://localhost:8888/callback"))

    SCOPES = [
        "user-read-currently-playing",
        "user-read-recently-played",
        "user-top-read"
    ]


def get_refresh_token(code: str) -> Dict[str, Any]:
    token = base64.b64encode(f"{Config.SPOTIFY_CLIENT_ID}:{Config.SPOTIFY_CLIENT_SECRET}".encode()).decode("utf-8")

    headers = {
        "Authorization": f"Basic {token}"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": Config.SPOTIFY_REDIRECT_URI,
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    return response.json()


url = generate_oauth_url(Config.SPOTIFY_CLIENT_ID, Config.SPOTIFY_REDIRECT_URI, Config.SCOPES)
print(f"Please visit the following URL to authorize the application: {url}")

code = input("Enter the value of code from URL query parameter: ")

if not code:
    raise Exception("No code provided.")


token = get_refresh_token(code)
print(f"Your refresh token is {token['refresh_token']}")
