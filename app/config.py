class LoggerConfig:
    # File to store logs.
    LOG_FILE = "logs/app.log"

    # Base level of logging.
    LOG_LEVEL = "INFO"

    # Other config.
    LOG_FORMAT = (
        "<green>{time:YYYY-MM-DD hh:mm:ss}</green> | <level>{level: <8}</level> | "
        "<cyan>{name: <18}</cyan> | <level>{message}</level>"
    )

    # Rotation size.
    LOG_FILE_SIZE = "400 MB"
