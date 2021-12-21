import sys

import tweepy
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

# Initialize the tweepy API.
auth = tweepy.OAuthHandler(Config.TWITTER_CONSUMER_KEY, Config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(Config.TWITTER_ACCESS_TOKEN, Config.TWITTER_ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth)
