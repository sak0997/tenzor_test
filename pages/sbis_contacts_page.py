from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from pages.base_page import BasePage
from pages.tensor_home_page import TensorHomePage


class SbisContactsPage(BasePage):

    TENSOR_BANNER = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')
    CURRENT_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    NEW_REGION = (By.XPATH, '//span[text()="41 Камчатский край"]')
    PARTNERS_LIST = (By.NAME, 'itemsContainer')
    PARTNERS_LIST_CITY = (By.CLASS_NAME, 'sbisru-Contacts-List__city')

    def click_tensor_banner(self):
        url = self.get_url_by_locator(self.TENSOR_BANNER)
        self.go_to_url(url)

        logger.info('Успешный клик на баннер Тензор.')

        return TensorHomePage(self.driver)

    def region_defined_correct(self):
        current_region = 'Республика Татарстан'

        current_region_is_right = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.CURRENT_REGION, current_region)
        )

        assert current_region_is_right

        logger.info('Регион в разделе Контакты определен корректно.')

    def partners_list_presented_and_visible(self):
        presented_and_visible = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PARTNERS_LIST)
        )

        assert presented_and_visible

        logger.info('Список партнеров в разделе Контакты показан корректно.')
    
    def change_region(self):
        current_region = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CURRENT_REGION)
        )

        current_region.click()

        new_region = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.NEW_REGION)
        )
        
        new_region.click()

        logger.info('Регион в разделе Контакты был изменен.')

    def region_changed_successfully(self):
        region = 'Камчатский край'

        region_is_right = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.CURRENT_REGION, region)
        )

        assert region_is_right

        logger.info('Регион в разделе Контакты изменен корректно.')
    
    def partners_list_changed_successfully(self):
        partners_city = 'Петропавловск-Камчатский'

        partners_list_city_is_right = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.PARTNERS_LIST_CITY, partners_city)
        )

        assert partners_list_city_is_right

        logger.info('Список партнеров в разделе Контакты изменен корректно.')

    def url_is_correct(self):
        url_region_string = '41-kamchatskij-kraj'

        correct_url = WebDriverWait(self.driver, 10).until(
            EC.url_contains(url_region_string)
        )

        assert correct_url

        logger.info('Url после изменения региона корректен.')

    def title_is_correct(self):
        title_region_string = 'Камчатский край'

        correct_title = WebDriverWait(self.driver, 10).until(
            EC.title_contains(title_region_string)
        )

        assert correct_title

        logger.info('Заголовок (title) после изменения региона корректен.')
