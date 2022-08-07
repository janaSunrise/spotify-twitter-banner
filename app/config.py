import os
from typing import Optional, cast

from decouple import config


class Config:
    # Debug mode
    DEBUG = cast(bool, config("DEBUG", default=False, cast=bool))

    # Update interval (in minutes)
    UPDATE_INTERVAL = cast(int, config("UPDATE_INTERVAL", default=2, cast=int))

    # Spotify refresh token for headless environments
    SPOTIFY_REFRESH_TOKEN = cast(Optional[str], config("SPOTIFY_REFRESH_TOKEN", default=None))

    # Spotify credentials
    SPOTIFY_CLIENT_ID = cast(str, config("SPOTIFY_CLIENT_ID"))
    SPOTIFY_CLIENT_SECRET = cast(str, config("SPOTIFY_CLIENT_SECRET"))

    # Twitter credentials
    TWITTER_CONSUMER_KEY = cast(str, config("TWITTER_CONSUMER_KEY"))
    TWITTER_CONSUMER_SECRET = cast(str, config("TWITTER_CONSUMER_SECRET"))
    TWITTER_ACCESS_TOKEN = cast(str, config("TWITTER_ACCESS_TOKEN"))
    TWITTER_ACCESS_TOKEN_SECRET = cast(str, config("TWITTER_ACCESS_TOKEN_SECRET"))

    # Redirect URI, Used for OAuth.
    SPOTIFY_REDIRECT_URI = cast(str, config("SPOTIFY_REDIRECT_URI", default="http://localhost:8888/callback"))

    # Spotify scopes
    SCOPES = [
        "user-read-currently-playing",
        "user-read-recently-played",
        "user-top-read"
    ]

    # Path to store the refresh token
    SPOTIFY_REFRESH_TOKEN_PATH = os.path.expanduser("~/.spotify_refresh_token")

    # Path to save the spotify banner image.
    IMAGE_PATH = "spotify-banner.jpeg"

    # Status for the song info.
    STATUS_MAPPING = {
        True: ["Vibing to", "Binging to", "Listening to", "Obsessed with"],
        False: ["Was listening to", "Previously binging to", "Was vibing to"]
    }

    # Github repository URL
    GITHUB_REPO_URL = "https://github.com/janaSunrise/Spotify-Twitter-Banner/"


class LoggerConfig:
    # File to store logs.
    LOG_FILE = "logs/app.log"

    # Base level of logging.
    LOG_LEVEL = "TRACE" if Config.DEBUG else "INFO"

    # Format of the log.
    LOG_FORMAT = (
        "<green>{time:YYYY-MM-DD hh:mm:ss}</green> | <level>{level: <8}</level> | "
        "<cyan>{name: <18}</cyan> | <level>{message}</level>"
    )

    # File Rotation size.
    LOG_FILE_SIZE = "500 MB"


class Fonts:
    # Base font path
    FONT_PATH = "app/assets/fonts/"

    FIRA_REGULAR = FONT_PATH + "FiraCode-Regular.ttf"
    FIRA_MEDIUM = FONT_PATH + "FiraCode-Medium.ttf"
    FIRA_SEMIBOLD = FONT_PATH + "FiraCode-SemiBold.ttf"

    POPPINS_REGULAR = FONT_PATH + "Poppins-Regular.ttf"
    POPPINS_SEMIBOLD = FONT_PATH + "Poppins-SemiBold.ttf"

    ARIAL = FONT_PATH + "arial-unicode-ms.ttf"
