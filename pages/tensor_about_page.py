from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from pages.base_page import BasePage


class TensorAboutPage(BasePage):

    WORKING_BLOCK_PHOTOS = (By.XPATH, '//img[contains(@class, "tensor_ru-About__block3-image")]')

    def url_is_valid(self):
        url = 'https://tensor.ru/about'

        url_valid = WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url)
        )

        assert url_valid

        logger.info('Успешный переход по адресу tensor.ru/about.')

    def all_photos_are_the_same_size(self):
        working_block_photos = self.find_all(self.WORKING_BLOCK_PHOTOS)

        width_list = []
        height_list = []

        for photo in working_block_photos:
            width_list.append(photo.get_attribute('width'))
            height_list.append(photo.get_attribute('height'))
        
        width_set = set(width_list)
        height_set = set(height_list)

        same_width = len(width_set) == 1
        same_height = len(height_set) == 1

        assert same_width and same_height
        
        logger.info('У всех фото раздела Работаем одинаковый размер.')
