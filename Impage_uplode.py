import requests
import base64

# Configuration
WORDPRESS_URL = "https://your_domain.com"
USERNAME = "your_username"
PASSWORD = "your_application_password"
AUTH = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode("utf-8")

def fetch_posts_without_featured_image():
    """Fetch posts without a featured image."""
    endpoint = f"{WORDPRESS_URL}/wp-json/wp/v2/posts?per_page=10&featured_media=0"
    headers = {"Authorization": f"Basic {AUTH}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def upload_image(image_path):
    """Upload an image to WordPress Media Library."""
    media_endpoint = f"{WORDPRESS_URL}/wp-json/wp/v2/media"
    headers = {
        "Authorization": f"Basic {AUTH}",
        "Content-Disposition": "attachment; filename={}".format(image_path.split("/")[-1]),
        "Content-Type": "image/jpeg",  # Adjust based on your image type
    }
    with open(image_path, "rb") as image:
        response = requests.post(media_endpoint, headers=headers, data=image)
        response.raise_for_status()
    return response.json()

def update_post_with_featured_image(post_id, image_id):
    """Update a post with a featured image."""
    post_endpoint = f"{WORDPRESS_URL}/wp-json/wp/v2/posts/{post_id}"
    headers = {"Authorization": f"Basic {AUTH}"}
    payload = {"featured_media": image_id}
    response = requests.post(post_endpoint, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

# Example Usage
if __name__ == "__main__":
    posts = fetch_posts_without_featured_image()
    if posts:
        image_path = "/path/to/your/image.jpg"  # Update this path
        uploaded_image = upload_image(image_path)
        image_id = uploaded_image["id"]
        for post in posts:
            updated_post = update_post_with_featured_image(post["id"], image_id)
            print(f"Updated Post ID {post['id']} with featured image ID {image_id}")
    else:
        print("No posts without featured images found.")
