from dataclasses import dataclass

BASE_URL = "https://api.spotify.com/v1"


@dataclass
class Route:
    method: str
    path: str

    @property
    def url(self) -> str:
        return BASE_URL + self.path
