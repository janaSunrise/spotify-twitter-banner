import sys

from loguru import logger

from .api.spotify import Spotify
from .config import Config, LoggerConfig

# Configure logging
logger.configure(
    handlers=[
        dict(
            sink=sys.stdout,
            format=LoggerConfig.LOG_FORMAT,
            level=LoggerConfig.LOG_LEVEL,
        ),
        dict(
            sink=LoggerConfig.LOG_FILE,
            format=LoggerConfig.LOG_FORMAT,
            level=LoggerConfig.LOG_LEVEL,
            rotation=LoggerConfig.LOG_FILE_SIZE,
        ),
    ]
)

# Initialize the Spotify API.
spotify = Spotify(Config.SPOTIFY_CLIENT_ID, Config.SPOTIFY_CLIENT_SECRET)
