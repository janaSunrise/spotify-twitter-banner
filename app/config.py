import os

from decouple import config


class Config:
    # Spotify credentials
    SPOTIFY_CLIENT_ID = config("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")

    # Redirect URI
    SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

    # Spotify Scopes
    SCOPES = [
        "user-read-currently-playing",
        "user-read-recently-played",
        "user-top-read"
    ]

    # Path to store the refresh token
    SPOTIFY_REFRESH_TOKEN_PATH = os.path.expanduser("~/.spotify_refresh_token")

    # Image save path.
    IMAGE_PATH = "spotify-banner.jpeg"


class LoggerConfig:
    # File to store logs.
    LOG_FILE = "logs/app.log"

    # Base level of logging.
    LOG_LEVEL = "INFO"

    # Other config.
    LOG_FORMAT = (
        "<green>{time:YYYY-MM-DD hh:mm:ss}</green> | <level>{level: <8}</level> | "
        "<cyan>{name: <18}</cyan> | <level>{message}</level>"
    )

    # Rotation size.
    LOG_FILE_SIZE = "400 MB"


class Fonts:
    # Base font path
    FONT_PATH = "app/assets/fonts/"

    # Fira code
    FIRA_REGULAR = FONT_PATH + "FiraCode-Regular.ttf"
    FIRA_MEDIUM = FONT_PATH + "FiraCode-Medium.ttf"
    FIRA_SEMIBOLD = FONT_PATH + "FiraCode-SemiBold.ttf"

    # Poppins
    POPPINS_REGULAR = FONT_PATH + "Poppins-Regular.ttf"
    POPPINS_SEMIBOLD = FONT_PATH + "Poppins-SemiBold.ttf"

    # Arial
    ARIAL = FONT_PATH + "arial-unicode-ms.ttf"
