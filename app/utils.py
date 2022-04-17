import random
import typing as t

from .models import Song

if t.TYPE_CHECKING:
    from .api.spotify import Spotify


# Generate the OAuth2 URL for spotify
def generate_oauth_url(client_id: str, redirect_uri: str, scopes: list) -> str:
    return f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri=" \
           f"{redirect_uri}&scope={','.join(scopes)}"


# Parse JSON data for song into Song object.
def get_song_info(spotify: "Spotify") -> t.Tuple[dict, bool]:
    # Get the currently playing track.
    now_playing = spotify.currently_playing()

    # Check if song is playing.
    if now_playing is not None and now_playing != {}:
        song = now_playing["item"]

        # Update all properties from now_playing.
        song.update(now_playing)

        # Ensure that there is a currently playing type.
        if not now_playing.get("currently_playing_type"):
            song["currently_playing_type"] = now_playing["currently_playing_type"]

        is_now_playing = now_playing["is_playing"]
    else:
        # Get recently played songs.
        recently_played = spotify.recently_played()

        # Get a random song.
        size_recently_played = len(recently_played["items"])
        idx = random.randint(0, size_recently_played - 1)

        song = recently_played["items"][idx]["track"]

        # Update properties from recently_played.
        song.update(recently_played)

        # Add track type.
        song["currently_playing_type"] = "track"

        is_now_playing = False

    return song, is_now_playing
