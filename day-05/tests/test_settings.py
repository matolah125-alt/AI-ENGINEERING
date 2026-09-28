import pytest

from config_manager.settings import get_app_environment, get_app_name


def test_get_app_name_returns_environment_value(monkeypatch):
	monkeypatch.setenv("APP_NAME", "My AI App")

	assert get_app_name() == "My AI App"


def test_get_app_name_returns_default_when_app_name_is_missing(monkeypatch):
	monkeypatch.delenv("APP_NAME", raising=False)

	assert get_app_name() == "AI Engineering App"


def test_get_app_environment_returns_environment_value(monkeypatch):
	monkeypatch.setenv("APP_ENV", "production")

	assert get_app_environment() == "production"


def test_get_app_environment_accepts_testing(monkeypatch):
	monkeypatch.setenv("APP_ENV", "testing")

	assert get_app_environment() == "testing"


def test_get_app_environment_returns_default_when_app_env_is_missing(monkeypatch):
	monkeypatch.delenv("APP_ENV", raising=False)

	assert get_app_environment() == "development"


def test_get_app_environment_rejects_invalid_value(monkeypatch):
	monkeypatch.setenv("APP_ENV", "banana")

	with pytest.raises(ValueError):
		get_app_environment()
