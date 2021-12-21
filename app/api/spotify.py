import base64
import json
import sys
import time
import typing as t

import requests
from loguru import logger

from ..config import Config
from ..utils import generate_oauth_url

PYTHON_VERSION = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


class Spotify:
    RETRY_ATTEMPTS = 5
    USER_AGENT = f"Spotify Twitter Banner - Python/{PYTHON_VERSION} Requests/{requests.__version__}"

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

        self.bearer_info = None
        self.refresh_token = self.load_refresh_token()

    # Get bearer info.
    def get_bearer_info(self) -> dict:
        if not self.refresh_token:
            raise Exception("No refresh token provided.")

        token = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode("utf-8")

        headers = {"Authorization": f"Basic {token}"}
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        # Get the bearer info.
        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

        # Check if the request was successful.
        if response.status_code != 200:
            raise Exception("Failed to get bearer info.")

        # Return the bearer info.
        info = response.json()

        if "error" in info:
            raise Exception(f"Failed to get bearer info: {info['error']}")

        return info

    # Function to get the refresh token from code.
    def get_refresh_token(self, code: str) -> dict:
        token = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode("utf-8")

        # Headers and data.
        headers = {
            "Authorization": f"Basic {token}"
        }
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Config.SPOTIFY_REDIRECT_URI,
        }

        # Post.
        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

        return response.json()

    # Function to handle loading refresh token.
    def load_refresh_token(self) -> str:
        # Load JSON and get refresh token.
        with open(Config.SPOTIFY_REFRESH_TOKEN_PATH, "r") as file:
            token = json.load(file)

        # Check if refresh token exists.
        if "refresh_token" not in token:
            logger.info("No refresh token found. Please follow the steps to get the refresh token.")

            # Generate OAuth URL.
            url = generate_oauth_url(self.client_id, Config.SPOTIFY_REDIRECT_URI, Config.SCOPES)
            print(f"Please visit the following URL to authorize the application: {url}")

            # Wait for user to input code.
            code = input("Enter the value of code from URL query parameter: ")

            # Handle input.
            if not code:
                raise Exception("No code provided.")

            # Get refresh token.
            token = self.get_refresh_token(code)

            # Calculate expired time
            expires_in = int(token["expires_in"])
            expires_at = time.time() + expires_in
            token["expires_at"] = expires_at

            # Save refresh token.
            with open(Config.SPOTIFY_REFRESH_TOKEN_PATH, "w") as file:
                json.dump(token, file)

        # Return refresh token.
        return token["refresh_token"]
