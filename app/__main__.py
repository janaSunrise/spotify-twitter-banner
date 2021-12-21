from . import spotify

# Get top tracks.
top_tracks = spotify.top_tracks()

# Assert it exists.
assert top_tracks is not None
