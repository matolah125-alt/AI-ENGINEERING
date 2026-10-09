import requests

from config import get_api_base_url


# Validate the requested user before making an HTTP request
def get_user(user_id, timeout=5):
    if isinstance(user_id, bool) or not isinstance(user_id, int):
        raise TypeError("user_id must be an integer")
    if user_id <= 0:
        raise ValueError("user_id must be positive")

    # Build the endpoint from the configured API host
    base_url = get_api_base_url().rstrip("/")
    url = f"{base_url}/users/{user_id}"

    # Return JSON for success, None for not-found, and propagate other failures
    try:
        response = requests.get(
            url,
            timeout=timeout,
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return None
        raise

    return response.json()