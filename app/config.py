import os

from decouple import config


class Config:
    # Debug mode.
    DEBUG = config("DEBUG", default=False, cast=bool)

    # Spotify credentials
    SPOTIFY_CLIENT_ID = config("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")

    # Twitter credentials
    TWITTER_CONSUMER_KEY = config("TWITTER_CONSUMER_KEY")
    TWITTER_CONSUMER_SECRET = config("TWITTER_CONSUMER_SECRET")
    TWITTER_ACCESS_TOKEN = config("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = config("TWITTER_ACCESS_TOKEN_SECRET")

    # Redirect URI, Used for OAuth.
    SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

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

    # Fira code
    FIRA_REGULAR = FONT_PATH + "FiraCode-Regular.ttf"
    FIRA_MEDIUM = FONT_PATH + "FiraCode-Medium.ttf"
    FIRA_SEMIBOLD = FONT_PATH + "FiraCode-SemiBold.ttf"

    # Poppins
    POPPINS_REGULAR = FONT_PATH + "Poppins-Regular.ttf"
    POPPINS_SEMIBOLD = FONT_PATH + "Poppins-SemiBold.ttf"

    # Arial
    ARIAL = FONT_PATH + "arial-unicode-ms.ttf"
