import tweepy

from .config import Config


# Function to update the twitter banner of the current profile using the image specified in config.
def update_twitter_banner(api: tweepy.API) -> None:
    api.update_profile_banner(Config.IMAGE_PATH)
