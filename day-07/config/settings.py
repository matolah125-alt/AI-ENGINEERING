import os


# Used when API_BASE_URL is not set in the process environment
DEFAULT_API_BASE_URL = "https://jsonplaceholder.typicode.com"


# Read the API host from the environment, falling back to the public default
def get_api_base_url():
    return os.environ.get("API_BASE_URL", DEFAULT_API_BASE_URL)
