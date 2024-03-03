from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from pages.base_page import BasePage
from pages.tensor_about_page import TensorAboutPage


class TensorHomePage(BasePage):

    PEOPLE_STRENGTH_TITLE = (By.XPATH, '//div[contains(@class, "tensor_ru-Index__block4-content")]/p[1]')
    TENSOR_ABOUT_LINK = (By.XPATH, '//a[@href="/about" and contains(@class, "tensor_ru-link")]')

    def url_is_valid(self):
        tensor_url = 'https://tensor.ru/'

        tensor_url_valid = WebDriverWait(self.driver, 10).until(
            EC.url_to_be(tensor_url)
        )

        assert tensor_url_valid

        logger.info('По ссылке Подробнее открывается верхная страница.')

    def people_strength_block_is_presented(self):
        title = 'Сила в людях'

        block_is_presented = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.PEOPLE_STRENGTH_TITLE, title)
        )

        assert block_is_presented

        logger.info('Блок Сила в людях есть на странице.')

    def go_to_tensor_about(self):
        url = self.get_url_by_locator(self.TENSOR_ABOUT_LINK)
        self.go_to_url(url)

        logger.info('Переход по ссылке Подробнее.')

        return TensorAboutPage(self.driver)
