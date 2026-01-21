import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler
import os

# Carpeta de logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # crea la carpeta si no existe

LOG_FILE = os.path.join(LOG_DIR, "resQLink.log")

def setup_logging():
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": "DEBUG",
            },
            "file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": LOG_FILE,            # process.log
                "formatter": "default",
                "level": "DEBUG",
                "encoding": "utf-8",
                "when": "midnight",
                "backupCount": 30,
                "utc": False
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["console", "file"]
        },
    }

    logging.config.dictConfig(logging_config)

    # Custom namer para poner el sufijo ANTES de .log
    for handler in logging.getLogger().handlers:
        if isinstance(handler, TimedRotatingFileHandler):

            def namer(name):
                base, date = name.rsplit(".", 1)

                return f"{base.replace('.log','')}-{date}.log"

            handler.namer = namer