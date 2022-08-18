import base64
import json
import sys
import time
from typing import Any, Dict, Literal, Optional, cast

import requests
from loguru import logger

from .route import Route
from ..config import Config

PYTHON_VERSION = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


class Spotify:
    RETRY_ATTEMPTS = 3
    USER_AGENT = f"Spotify Twitter Banner ({Config.GITHUB_REPO_URL}) - Python/{PYTHON_VERSION} Requests/{requests.__version__}"

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

        self.bearer_info = None
        self.refresh_token = Config.SPOTIFY_REFRESH_TOKEN

    def get_bearer_info(self) -> Dict[str, Any]:
        """Get the bearer info containing the access token to access the spotify endpoints."""
        if not self.refresh_token:
            raise Exception("No refresh token provided.")

        token = self.generate_base64_token()

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

    def get_refresh_token(self, code: str) -> Dict[str, Any]:
        """Get the spotify refresh token using the `code` obtained after the OAuth2 authorization
        flow present in the URL.
        """
        token = self.generate_base64_token()

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

    def fetch(
        self,
        route: Route,
        *,
        headers: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None
    ) -> Optional[Dict[str, Any]]:
        if not headers:
            headers = {}

        # Check if Authorization exists.
        if "Authorization" not in headers:
            # Check if bearer info exists.
            if self.bearer_info is None:
                self.bearer_info = self.get_bearer_info()

            # Set the Authorization header.
            headers["Authorization"] = f"Bearer {self.bearer_info['access_token']}"

        headers = {
            "User-Agent": self.USER_AGENT,
            "Content-Type": "application/json",
            **headers
        }

        # Perform request with retries.
        for _ in range(self.RETRY_ATTEMPTS):
            response = requests.request(route.method, route.url, headers=headers, json=data)

            logger.debug(f"[{route.method}] ({response.status_code}) {route.url}")

            # Check if the request was successful.
            if response.status_code == 200:
                return response.json()

            try:
                data = json.loads(response.text)
            except json.decoder.JSONDecodeError:
                data = None

            if 200 <= response.status_code < 300:
                return data

            # Handle ratelimited requests
            if response.status_code == 429:
                retry_after = int(response.headers["Retry-After"])

                logger.info(f"Ratelimited, Waiting for {retry_after} seconds.")
                time.sleep(retry_after)

                continue

            # Handle access token expired
            if response.status_code == 401:
                logger.info("Bearer info expired, Refreshing.")
                self.bearer_info = self.get_bearer_info()

                continue

            # Ignore anything 5xx
            if response.status_code >= 500:
                continue

            # Route not found error - This won't happen most of the times
            if response.status_code == 404:
                logger.warning(f"Failed to fetch: {route.url} - Route not found.")
                return None

            # If it's an internal route for the app
            if response.status_code == 403:
                logger.warning(f"Failed to fetch: {route.url} - Forbidden route.")
                return None

    # Utility methods
    def generate_base64_token(self) -> str:
        return base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode("utf-8")

    @staticmethod
    def _form_url(url: str, data: Dict[str, Any]) -> str:
        url += "?" + "&".join([f"{dict_key}={dict_value}" for dict_key, dict_value in data.items()])

        return url

    # Main endpoints
    def currently_playing(self) -> Optional[Dict[str, Any]]:
        """Get the currently playing song/podcast."""
        route = Route(
            "GET",
            self._form_url("/me/player/currently-playing", {
                "additional_types": "track,episode"
            })
        )

        return self.fetch(route)

    def is_playing(self) -> bool:
        """Check if the user is currently listening to music."""
        currently_playing = self.currently_playing()

        if currently_playing:
            return currently_playing["is_playing"]

        return False

    def recently_played(
        self,
        limit: int = 20,
        before: Optional[str] = None,
        after: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get recently played tracks."""
        data: Dict[str, Any] = {"limit": limit}

        if before:
            data["before"] = before

        if after:
            data["after"] = after

        route = Route(
            "GET",
            self._form_url("/me/player/recently-played", data)
        )

        return cast(Dict[str, Any], self.fetch(route))

    def top_tracks(
        self,
        limit: int = 20,
        offset: int = 0,
        time_range: Optional[Literal["short_term", "medium_term", "long_term"]] = None
    ) -> Dict[str, Any]:
        """Get top tracks of the user."""
        data: Dict[str, Any] = {
            "limit": limit,
            "offset": offset
        }

        if time_range:
            data["time_range"] = time_range

        route = Route(
            "GET",
            self._form_url("/me/top/tracks", data)
        )

        return cast(Dict[str, Any], self.fetch(route))
