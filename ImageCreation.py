from PIL import Image, ImageDraw, ImageFont
import os
from random import choice as choiceImageFrom

def image_creation(text_title):
    """
    Creates an Image by saving it in a PNG file,
    :param text_title: title of the image
    :return: Path of image
    """
    # Ensure the Resources directory path is correct
    resources_path = "Resources"
    if not os.path.isdir(resources_path):
        raise ValueError(f"Directory not found: {resources_path}")

    # Load the image file
    img_path = os.path.join(resources_path, choiceImageFrom(os.listdir(resources_path)))
    img = Image.open(img_path)

    # Define font size and color
    font_size = 50
    font_color = (255, 255, 255)  # White color

    # Define font object (standard PIL font)
    font_path = "font/dejavu-sans/DejaVuSans-Bold.ttf"
    font_title = ImageFont.truetype(font_path, font_size)

    # Calculate text length
    text_length = font_title.getlength(text_title)  # Width of the text

    # Calculate text height (font size * number of lines)
    num_lines = text_title.count('\n') + 1  # Count the number of newline characters
    text_height = font_size * num_lines

    # Calculate text position
    text_x = (img.width - text_length) / 2
    text_y = (img.height - text_height) / 2

    # Create draw object
    draw = ImageDraw.Draw(img)

    # Draw text on image
    draw.text((text_x, text_y), text_title, font=font_title, fill=font_color)

    # Define the path for saving the new image
    new_img_path = f'Images/{text_title}.png'
    # Ensure the directory exists
    os.makedirs(os.path.dirname(new_img_path), exist_ok=True)

    img.save(new_img_path)  # Save the new image

    return new_img_path
