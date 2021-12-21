# Function to generate OAuth URL.
def generate_oauth_url(client_id, redirect_uri, scopes):
    return f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri=" \
           f"{redirect_uri}&scope={','.join(scopes)}"
