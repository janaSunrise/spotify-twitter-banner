import tweepy

from .config import Config


def update_twitter_banner(api: tweepy.API) -> None:
    """Update the twitter banner of the current profile using the image specified in config."""
    api.update_profile_banner(Config.IMAGE_PATH)
