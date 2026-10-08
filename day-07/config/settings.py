import os


DEFAULT_API_BASE_URL = "https://jsonplaceholder.typicode.com"


def get_api_base_url():
    return os.environ.get("API_BASE_URL", DEFAULT_API_BASE_URL)
