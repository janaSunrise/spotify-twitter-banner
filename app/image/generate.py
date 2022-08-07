from typing import cast

from PIL import Image, ImageDraw, ImageFont

from ..config import Fonts
from ..models.song import Song


def truncate_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> str:
    if font.getsize(text)[0] <= max_width:
        return text.strip()

    while font.getsize(text)[0] > max_width:
        text = text[:-1]

    return text.strip() + ".."


def midpoint(start: int, end: int, text: str, font: ImageFont.FreeTypeFont) -> float:
    """Calculate the midpoint between two points with the text width of the font."""
    mid = (start + end) / 2

    text_width = font.getsize(text)[0]

    return mid - (text_width / 2)


def draw_tag(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, font: ImageFont.FreeTypeFont, color: tuple) -> None:
    """Draw a tag with black text and specified color as background."""
    draw.rectangle((x, y, x + font.getsize(text)[0] + 10, y + font.getsize(text)[1] + 10), fill=color)
    draw.text((x + 5, y + 5), text, font=font, fill=(0, 0, 0))


def generate_image(
    status: str,
    song: Song,
    top_tracks: list,
    image_save_path: str,
    show_only: bool = False
) -> None:
    # Get the top tracks filtered by grabbing the name, and artist.
    top_tracks = [
        {
            "name": track["name"].replace("&", "&amp;"),
            "artist": track["artists"][0]["name"].replace("&", "&amp;"),
        }
        for track in top_tracks
    ]

    # Create an image.
    img = Image.new("RGB", (1500, 500), (10, 14, 18))
    draw = ImageDraw.Draw(img)

    # Load fonts
    fira_code = ImageFont.truetype(Fonts.FIRA_REGULAR, size=23)
    fira_code_small = ImageFont.truetype(Fonts.FIRA_REGULAR, size=18)
    poppins = ImageFont.truetype(Fonts.POPPINS_REGULAR, size=27)
    poppins_semibold = ImageFont.truetype(Fonts.POPPINS_SEMIBOLD, size=27)

    # Add the song image to the image.
    song.image.thumbnail((350, 350), Image.ANTIALIAS)
    img.paste(song.image, (50, 100))

    # Add the status text above the image, aligned in the center, using midpoint from coordinates of 50 to 400.
    draw.text(
        (50, 50),
        status,
        (255, 255, 255),
        font=poppins,
    )

    # Add the song name, artist name, and album name in the right side of the image.
    white = "#ffffff"

    draw.text(
        (400, 150),
        truncate_text(song.name, poppins, 600),
        fill=white,
        font=poppins_semibold,
    )

    draw.text(
        (400, 200),
        truncate_text(song.artist, poppins, 600),
        fill=white,
        font=poppins,
    )

    draw.text(
        (400, 250),
        truncate_text(song.album, poppins, 600),
        fill=white,
        font=poppins,
    )

    # Add explicit tag.
    if song.is_explicit:
        draw_tag(draw, 400, 300, "EXPLICIT", fira_code_small, (255, 255, 255))

    # Add a white line in left of top tracks, to separate it.
    draw.line(
        (
            img.size[0] - 375,
            100,
            img.size[0] - 375,
            400,
        ),
        fill=white
    )

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
        (img.size[0] - 350, 50),
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

        # Add the artist name.
        draw.text(
            (
                img.size[0] - 350,
                100 + (i * 50) + (i * 10) + 35,
            ),
            track["artist"],
            font=fira_code_small,
            fill=(255, 255, 255),
        )

    # Add song progress bar, if listening currently.
    if song.is_now_playing:
        total_time = cast(int, song.duration_ms)
        current_time = cast(int, song.progress_ms)

        # Calculate the progress bar width.
        progress_bar_width = (current_time / total_time) * 700

        # Draw the progress bar. White for the covered progress, Gray for the left progress.
        # Draw from right of the image till the top tracks.
        draw.rectangle(
            ((375, 425), (1100, 430)),
            fill="#B3B3B3"
        )
        draw.rectangle(
            ((375 + progress_bar_width, 425), (1100, 430)), fill="#404040"
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

    # Show the image, if show only is enabled.
    if show_only:
        img.show()
    else:
        # Save the image to the path specified.
        img.save(image_save_path, format="JPEG", quality=100)
