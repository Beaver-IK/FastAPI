import logging


def setup_logger():
    """Функция настройки логгера."""
    logger = logging.getLogger('first_project')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


LOGGER = setup_logger()
