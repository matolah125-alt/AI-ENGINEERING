import logging
from pathlib import Path


def get_logger(
    name: str, log_file: str | Path | None = None
) -> logging.Logger:
    """Return an INFO-level logger that writes formatted messages to a file."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        log_path = (
            Path(log_file)
            if log_file is not None
            else Path(__file__).resolve().parents[1] / "logs" / "app.log"
        )
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger