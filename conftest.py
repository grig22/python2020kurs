import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s %(funcName)s] %(message)s",
    handlers=[
        logging.FileHandler("debug22.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
