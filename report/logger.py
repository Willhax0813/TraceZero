# report/logger.py

import logging
import os
from datetime import datetime
from config.settings import LOG_LEVEL, OUTPUT_DIR


def init_logger():
    log_dir = os.path.join(OUTPUT_DIR, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"tracezero_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logger = logging.getLogger("TRACEZERO")
    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s", "%H:%M:%S")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Bind handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("[+] Logger initialized.")
    return logger
