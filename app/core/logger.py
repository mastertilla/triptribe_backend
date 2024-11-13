import logging.config
from pathlib import Path

cwd = Path(__file__).parent
output_path = cwd / 'logging.conf'

logging.config.fileConfig(fname=output_path, disable_existing_loggers=False)
logger = logging.getLogger()
