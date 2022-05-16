import random

from app import spotify
from app.config import Config
from app.image.generate import generate_image
from app.utils import get_song_info

# Get top tracks.
top_tracks = spotify.top_tracks(limit=5)

top_tracks = [track for track in top_tracks["items"]]

# Get song info with switch to recently played if no song is playing.
song = get_song_info(spotify=spotify)

# Get the status.
status = random.choice(Config.STATUS_MAPPING[song.is_now_playing]) + ":"

# Generate the spotify banner image, and display it.
generate_image(status, song, top_tracks, Config.IMAGE_PATH, show_only=True)
