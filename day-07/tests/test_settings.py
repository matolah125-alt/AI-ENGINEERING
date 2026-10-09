from config import get_api_base_url


# API URL environment override and default
def test_get_api_base_url_uses_environment_variable(monkeypatch):
    monkeypatch.setenv("API_BASE_URL", "https://api.example.com")

    assert get_api_base_url() == "https://api.example.com"


def test_get_api_base_url_uses_default_when_environment_variable_is_missing(
    monkeypatch,
):
    monkeypatch.delenv("API_BASE_URL", raising=False)

    assert get_api_base_url() == "https://jsonplaceholder.typicode.com"
