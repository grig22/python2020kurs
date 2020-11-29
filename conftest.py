import logging
import sys
import pytest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s %(funcName)s] %(message)s",
    handlers=[
        logging.FileHandler("main.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


@pytest.fixture(scope="session")
def testlog():
    logger = logging.getLogger("TESTLOG")
    logger.info("TESTLOG INIT")
    return logger


@pytest.fixture(autouse=True, scope="function")
def current(testlog, request):
    testlog.info(f">>>> START '{request.node.name}'")
    yield
    testlog.info(f"<<<< FINISH '{request.node.name}'")
