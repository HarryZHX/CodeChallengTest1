import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

@pytest.fixture(scope='class')
def init_driver(request):
        web_driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        request.cls.driver = web_driver
        web_driver.implicitly_wait(10)
        yield
        web_driver.close()
