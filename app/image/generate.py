from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

from ..config import Fonts


def truncate_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> str:
    if font.getsize(text)[0] <= max_width:
        return text.strip()

    while font.getsize(text)[0] > max_width:
        text = text[:-1]

    return text.strip() + ".."


def load_image_from_url(url: str) -> Image.Image:
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


# Function to calculate the mid point based on the start and end points, and the text to be written.
def midpoint(start: int, end: int, text: str, font: ImageFont.FreeTypeFont) -> int:
    mid = (start + end) / 2

    text_width = font.getsize(text)[0]

    return mid - (text_width / 2)


# Function to display tag - Background as white, and Text as black in a small rounded rectangle.
def draw_tag(draw: ImageDraw.Draw, x: int, y: int, text: str, font: ImageFont.FreeTypeFont, color: tuple) -> None:
    draw.rectangle((x, y, x + font.getsize(text)[0] + 10, y + font.getsize(text)[1] + 10), fill=color)
    draw.text((x + 5, y + 5), text, font=font, fill=(0, 0, 0))


def get_song_data(song: dict) -> dict:
    # Get the song type.
    currently_playing_type = song.get("currently_playing_type", "track")

    # Load name, artist, image, is_explicit.
    song_name, artist_name, img, is_explicit, album_name = None, None, None, None, None

    if currently_playing_type == "track":
        artist_name = song["artists"][0]["name"].replace("&", "&amp;")
        song_name = song["name"].replace("&", "&amp;")
        album_name = song["album"]["name"].replace("&", "&amp;")

        img = load_image_from_url(song["album"]["images"][1]["url"])
    elif currently_playing_type == "episode":
        artist_name = song["show"]["publisher"].replace("&", "&amp;")
        song_name = song["name"].replace("&", "&amp;")
        album_name = song["show"]["name"].replace("&", "&amp;")

        img = load_image_from_url(song["images"][1]["url"])

    is_explicit = song["explicit"]

    return song_name, f"By {artist_name}", img, is_explicit, f"On {album_name}"


def generate_image(status: str, is_playing: bool, song: dict, top_tracks: list, image_save_path: str) -> None:
    # Process the songs and top tracks.
    song_name, artist_name, song_image, is_explicit, album_name = get_song_data(song)

    # Get the top tracks filtered by grabbing the name, and artist.
    top_tracks = [
        {
            "name": track["name"].replace("&", "&amp;"),
            "artist": track["artists"][0]["name"].replace("&", "&amp;"),
        }
        for track in top_tracks
    ]

    # Create an image of size - 1200x675
    img = Image.new("RGB", (1500, 500), (18, 18, 18))
    draw = ImageDraw.Draw(img)

    # Load fonts
    fira_code = ImageFont.truetype(Fonts.FIRA_REGULAR, size=23)
    fira_code_small = ImageFont.truetype(Fonts.FIRA_REGULAR, size=18)
    poppins = ImageFont.truetype(Fonts.POPPINS_REGULAR, size=27)
    poppins_semibold = ImageFont.truetype(Fonts.POPPINS_SEMIBOLD, size=27)

    # Add the song image to the image.
    song_image.thumbnail((350, 350), Image.ANTIALIAS)
    img.paste(song_image, (50, 100))

    # Add the status text above the image, aligned in the center, using midpoint from coordinates of 50 to 400.
    draw.text(
        (midpoint(50, 350, status, fira_code), 50),
        status,
        (255, 255, 255),
        font=poppins,
    )

    # Add the song name, artist name, and album name in the right side of the image.
    white = "#ffffff"

    draw.text(
        (400, 150),
        truncate_text(song_name, poppins, 350),
        fill=white,
        font=poppins_semibold,
    )

    draw.text(
        (400, 200),
        truncate_text(artist_name, poppins, 350),
        fill=white,
        font=poppins,
    )

    draw.text(
        (400, 250),
        truncate_text(album_name, poppins, 350),
        fill=white,
        font=poppins,
    )

    # Add explicit tag.
    if is_explicit:
        draw_tag(draw, 400, 300, "EXPLICIT", fira_code_small, (255, 255, 255))

    # Assign top songs name and artists font.
    top_tracks = [
        {
            "name": truncate_text(track["name"], poppins, 300),
            "artist": truncate_text(track["artist"], fira_code, 300),
        }
        for track in top_tracks
    ]

    # Add title containing top tracks on top before displaying the top tracks.
    draw.text(
        (
            img.size[0] - 350,
            50,
        ),
        "Top Tracks:",
        fill=white,
        font=poppins_semibold,
    )

    # Add the top songs to the right side of the image.
    for i, track in enumerate(top_tracks):
        # Add the song name.
        draw.text(
            (
                img.size[0] - 350,
                100 + (i * 50) + (i * 10),
            ),
            track["name"],
            font=poppins,
            fill=(255, 255, 255),
        )

        # Add the artist name, after explicit tag.
        draw.text(
            (
                img.size[0] - 350,
                100 + (i * 50) + (i * 10) + 30,
            ),
            track["artist"],
            font=fira_code_small,
            fill=(255, 255, 255),
        )

    # Add song progress bar, if listening currently.
    if is_playing:
        total_time = song["duration_ms"]
        current_time = song["progress_ms"]

        # Calculate the progress bar width.
        progress_bar_width = (current_time / total_time) * 700

        # Draw the progress bar. White for the covered progress, Gray for the left progress.
        # Draw from right of the image till the top tracks.
        draw.rectangle(
            [(375, 425), (1100, 430)],
            fill="#B3B3B3"
        )
        draw.rectangle(
            [(375 + progress_bar_width, 425), (1100, 430)], fill="#404040"
        )

        # Add the time progress text, in the center of the progress bar. Display current time and total time.
        current_progress = f"{current_time // 60000}:{current_time // 1000 % 60:02d}"
        total_progress = f"{total_time // 60000}:{total_time // 1000 % 60:02d}"

        # Display current progress in the progress bar start.
        draw.text(
            (
                375,
                440,
            ),
            current_progress,
            font=poppins,
            fill=(255, 255, 255),
        )

        # Display total progress in the progress bar end.
        draw.text(
            (
                1100 - (len(total_progress) * 10),
                440,
            ),
            total_progress,
            font=poppins,
            fill=(255, 255, 255),
        )

    # Save the image to the path specified.
    img.save(image_save_path, format="JPEG", quality=200)

    return
