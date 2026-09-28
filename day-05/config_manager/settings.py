from dotenv import load_dotenv
import os


def get_app_name() -> str:
	return os.getenv("APP_NAME", "AI Engineering App")


def get_app_environment() -> str:
	environment = os.getenv("APP_ENV", "development")
	if environment not in {"development", "testing", "production"}:
		raise ValueError(f"Invalid APP_ENV value: {environment}")
	return environment
