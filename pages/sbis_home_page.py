from selenium.webdriver.common.by import By
from loguru import logger
from pages.base_page import BasePage
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_download_page import SbisDownloadPage


class SbisHomePage(BasePage):

    CONTACTS_LINK = (By.XPATH, '//a[@href="/contacts" and contains(@class, "sbisru-Footer__link")]')
    SBIS_DOWNLOAD_PAGE_LINK = (By.LINK_TEXT, 'Скачать локальные версии')

    def go_to_contacts_page(self):
        url = self.get_url_by_locator(self.CONTACTS_LINK)
        self.go_to_url(url)

        logger.info('Успешный переход в раздел Контакты.')

        return SbisContactsPage(self.driver)

    def go_to_download_sbis(self):
        url = self.get_url_by_locator(self.SBIS_DOWNLOAD_PAGE_LINK)
        self.go_to_url(url)

        logger.info('Успешный переход в раздел Скачать.')

        return SbisDownloadPage(self.driver)
