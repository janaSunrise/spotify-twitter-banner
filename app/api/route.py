class Route:
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self, method: str, path: str) -> None:
        self.method = method
        self.path = path

    # Properties
    @property
    def base_url(self) -> str:
        return self.BASE_URL

    @base_url.setter
    def base_url(self, url: str) -> None:
        self.BASE_URL = url

    @property
    def url(self) -> str:
        return self.base_url + self.path
