# Function to generate OAuth URL.
def generate_oauth_url(client_id: str, redirect_uri: str, scopes: list) -> str:
    return f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri=" \
           f"{redirect_uri}&scope={','.join(scopes)}"
