from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def get_url_by_locator(self, locator):
        link = self.find(locator)
        url = link.get_attribute('href')

        return url

    def go_to_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.find(locator).click()
