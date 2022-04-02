import typing as t
from dataclasses import dataclass
from io import BytesIO


@dataclass
class Song:
    song: str
    artist: str
    album: str

    image_url: str
    image: BytesIO

    is_explicit: bool

    currently_playing_type: t.Literal["track", "episode"]
    is_now_playing: bool
