import base64

def authorization():

    # Configuration
    WORDPRESS_URL = ("[Web site url]")
    USERNAME = "[user name]"
    PASSWORD = "[app password]"
    AUTH = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode("utf-8")

    return AUTH, WORDPRESS_URL