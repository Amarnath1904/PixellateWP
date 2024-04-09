from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
from random import choice as ChoseImage

def image_creation(text_title):
    """
    Creates an Image with centered and wrapped text, saving it in a PNG file.
    :param text_title: Title of the image
    :return: Path of the generated image file
    """
    # Ensure the Resources directory path is correct
    resources_path = "Resources"
    if not os.path.isdir(resources_path):
        raise ValueError(f"Directory not found: {resources_path}")

    # Load a random image from the resources directory
    img_path = os.path.join(resources_path, ChoseImage(os.listdir(resources_path)))
    img = Image.open(img_path)

    draw = ImageDraw.Draw(img)

    # Define font properties
    font_size = 50
    font_color = "#FFFFFF"  # Wight for better visibility in example
    font_path = "font/dejavu-sans/DejaVuSans-Bold.ttf"
    font = ImageFont.truetype(font_path, font_size)

    # Wrap text after a certain number of characters for better appearance
    wrapped_text = "\n".join(textwrap.wrap(text_title, width=20))  # Adjust `width` based on your needs

    # Drawing text centered at the middle of the image
    draw.text(
        xy=(img.width / 2, img.height / 2),
        text=wrapped_text,
        fill=font_color,
        font=font,
        anchor="mm",
        align="center"
    )

    # Define path for saving the new image
    new_img_path = f'Images/{text_title}.png'
    new_img_path = new_img_path.replace("?", "")
    new_img_path = new_img_path.replace("&#038;", "and")

    os.makedirs(os.path.dirname(new_img_path), exist_ok=True)
    img.save(new_img_path)

    return new_img_path
