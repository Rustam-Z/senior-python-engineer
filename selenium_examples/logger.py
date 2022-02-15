# import logging logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(
# levelname)s - %(message)s')

import logging.config
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.getcwd() + "/logs/app.log", "a", "utf-8"),
        logging.StreamHandler()
    ],
)
logger = logging.getLogger(__name__)
