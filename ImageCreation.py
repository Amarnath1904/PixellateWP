from PIL import Image, ImageDraw, ImageFont

# Load the image file
img_path = '/mnt/data/image.png'
img = Image.open(img_path)

# Define the text to overlay on the image
text_title = "Game Loops in World of Warcraft: Part 2 of 2"
text_footer = "yukaichou.com"

# Define font size and color
font_size = 50
font_color = (255, 255, 255)  # White color

# Define font object (standard PIL font)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_title = ImageFont.truetype(font_path, font_size)
font_footer = ImageFont.truetype(font_path, int(font_size / 2))

# Calculate text size and position
draw = ImageDraw.Draw(img)
text_width, text_height = draw.textsize(text_title, font=font_title)
text_x = (img.width - text_width) / 2
text_y = img.height * 0.1  # 10% from the top

# Calculate footer position
footer_width, footer_height = draw.textsize(text_footer, font=font_footer)
footer_x = (img.width - footer_width) / 2
footer_y = img.height - footer_height - img.height * 0.05  # 5% from the bottom

# Draw text on image
draw.text((text_x, text_y), text_title, font=font_title, fill=font_color)
draw.text((footer_x, footer_y), text_footer, font=font_footer, fill=font_color)

# Save the new image
new_img_path = '/mnt/data/annotated_image.png'
img.save(new_img_path)

# Return the path to the saved image
new_img_path
