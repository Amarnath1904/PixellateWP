import base64

def authorization():

    # Configuration
    WORDPRESS_URL = "{site url}"
    USERNAME = "{user}"
    PASSWORD = "{wp application password}"
    AUTH = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode("utf-8")

    return AUTH, WORDPRESS_URL