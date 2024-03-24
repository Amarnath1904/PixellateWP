import requests
def posts_without_featured_image(WORDPRESS_URL, AUTH, page):


    """
    Fetch posts without featured image from Yukaichou WEBSIDE
    :param WORDPRESS_URL:
    :param AUTH:
    :return:
    """
    endpoint = f"{WORDPRESS_URL}/wp-json/wp/v2/posts?per_page=100&featured_media=0&page={page}"
    headers = {"Authorization": f"Basic {AUTH}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def upload_image(image_path, WORDPRESS_URL, AUTH):
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

def update_post_with_featured_image(post_id, image_id, WORDPRESS_URL, AUTH):
    """Update a post with a featured image."""
    post_endpoint = f"{WORDPRESS_URL}/wp-json/wp/v2/posts/{post_id}"
    headers = {"Authorization": f"Basic {AUTH}"}
    payload = {"featured_media": image_id}
    response = requests.post(post_endpoint, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


