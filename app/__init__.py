import sys

from loguru import logger

from .config import LoggerConfig

# Configure logging
logger.configure(
    handlers=[
        dict(
            sink=sys.stdout,
            format=LoggerConfig.LOG_FORMAT,
            level=LoggerConfig.LOG_LEVEL,
        ),
        dict(
            sink=LoggerConfig.LOG_FILE,
            format=LoggerConfig.LOG_FORMAT,
            level=LoggerConfig.LOG_LEVEL,
            rotation=LoggerConfig.LOG_FILE_SIZE,
        ),
    ]
)
