from unittest.mock import patch

import pytest
import requests

from api_client.client import get_user


@pytest.mark.parametrize(
    ("user_id", "expected_user"),
    [
        (1, {"id": 1, "name": "Test User 1"}),
        (2, {"id": 2, "name": "Test User 2"}),
        (50, {"id": 50, "name": "Test User 50"}),
    ],
)
def test_get_user_success(user_id, expected_user):
    with patch("api_client.client.requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected_user

        assert get_user(user_id) == expected_user
        mock_get.assert_called_once_with(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=5,
        )


def test_get_user_not_found():
    with patch("api_client.client.requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        assert get_user(999) is None
        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/999",
            timeout=5,
        )


def test_get_user_server_error():
    with patch("api_client.client.requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        with pytest.raises(requests.exceptions.HTTPError):
            get_user(5)

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/5",
            timeout=5,
        )


def test_get_user_connection_error():
    with patch("api_client.client.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()

        with pytest.raises(requests.exceptions.ConnectionError):
            get_user(1)

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=5,
        )


def test_get_user_timeout():
    with patch("api_client.client.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout()

        with pytest.raises(requests.exceptions.Timeout):
            get_user(1, timeout=2)

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=2,
        )


@pytest.mark.parametrize(
    ("user_id", "error_type"),
    [
        (0, ValueError),
        (-1, ValueError),
        ("abc", TypeError),
        (1.5, TypeError),
    ],
)
def test_get_user_invalid_id_does_not_make_request(user_id, error_type):
    with patch("api_client.client.requests.get") as mock_get:
        with pytest.raises(error_type):
            get_user(user_id)

        mock_get.assert_not_called()


def test_get_user_uses_custom_api_base_url(monkeypatch):
    monkeypatch.setenv("API_BASE_URL", "https://api.example.com")

    with patch("api_client.client.requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 7, "name": "Custom API User"}

        assert get_user(7) == {"id": 7, "name": "Custom API User"}
        mock_get.assert_called_once_with(
            "https://api.example.com/users/7",
            timeout=5,
        )