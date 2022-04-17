import typing as t
from dataclasses import dataclass, field
from io import BytesIO

import requests


@dataclass
class Song:
    song: str
    artist: str
    album: str

    is_explicit: bool

    currently_playing_type: t.Literal["track", "episode"]
    is_now_playing: bool

    image_url: str
    image: BytesIO = field(init=False, repr=False)

    def __post_init__(self):
        self.image = BytesIO(requests.get(self.image_url).content)
