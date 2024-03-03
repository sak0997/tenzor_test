import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    url = "https://sbis.ru/"
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
