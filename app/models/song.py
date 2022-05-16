import typing as t
from dataclasses import dataclass, field
from io import BytesIO

import requests
from PIL import Image


@dataclass
class Song:
    name: str
    artist: str
    album: str

    is_explicit: bool

    currently_playing_type: t.Literal["track", "episode"]
    is_now_playing: bool

    image_url: str
    image: Image.Image = field(init=False, repr=False)

    progress_ms: t.Optional[int]
    duration_ms: t.Optional[int]

    def __post_init__(self):
        self.image = Image.open(BytesIO(requests.get(self.image_url).content))

    @classmethod
    def from_json(cls, song: t.Dict[str, t.Any]) -> "Song":
        is_now_playing = song["is_now_playing"]
        currently_playing_type = song.get("currently_playing_type")

        progress_ms = song.get("progress_ms")
        duration_ms = song.get("duration_ms")

        artist_name = song["artists"][0]["name"].replace("&", "&amp;")
        song_name = song["name"].replace("&", "&amp;")
        album_name = song["album"]["name"].replace("&", "&amp;")

        img_url = song["album"]["images"][1]["url"]

        return cls(
            song_name,
            f"By {artist_name}",
            f"On {album_name}",
            song["explicit"],
            currently_playing_type,
            is_now_playing,
            img_url,
            progress_ms,
            duration_ms,
        )
