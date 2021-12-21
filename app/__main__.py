from . import spotify
from .utils import get_song_info

# Get top tracks.
top_tracks = spotify.top_tracks()

# Assert it exists.
assert top_tracks is not None

# Get song info.
song, is_now_playing = get_song_info(spotify)

# Assert song is not none.
assert song is not None

# Print out is_now_playing.
print(is_now_playing)
