import pytest
from setup.web_setup import web_driver

# For parallel tests
@pytest.fixture(scope="class")
def driver():
    driver = web_driver()
    yield driver
    driver.quit()
