import logging

LOGGER_CONFIGURATION = {
    'level': logging.INFO,
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}

logging.basicConfig(**LOGGER_CONFIGURATION)

logger = logging.getLogger(__name__)
