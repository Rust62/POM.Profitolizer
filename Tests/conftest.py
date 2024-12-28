
import pytest
from selenium import webdriver


# @pytest.fixture(params=["chrome", "firefox", 'MsEdge'], scope='class')
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    web_driver = None
    if request.param == "chrome":
        options = webdriver.Chrome()
        options.headless = False
        # options.delete_all_cookies()
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        options = webdriver.Firefox()
        options.headless = False
        web_driver = webdriver.Firefox()
    if request.param == "MsEdge":
        options = webdriver.Edge()
        options.headless = False
        web_driver = webdriver.Edge()
    request.cls.driver = web_driver

    web_driver.maximize_window()
    yield
    web_driver.quit()

# @pytest.fixture(params=["chrome", "firefox", 'MsEdge'], scope='class')
# https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#fixture-parametrize
