import time
import os
import wget

from selenium.webdriver.common.by import By
from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SbisDownloadPage(BasePage):

    SBIS_PLUGIN_TAB = (By.XPATH, '//div[contains(@class, "controls-TabButtons")]/div[2]')
    SBIS_DOWNLOAD_PLUGIN_LINK = (By.LINK_TEXT, 'Скачать (Exe 8.17 МБ)')

    def click_sbis_plugin_tab(self):
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SBIS_PLUGIN_TAB)
        ).click()

        logger.info('Успешный переход на вкладку СБИС Плагин.')

    def download_sbis_plugin(self):
        url = self.get_url_by_locator(self.SBIS_DOWNLOAD_PLUGIN_LINK)
        path = os.getcwd()

        logger.info('Началась загрузка плагина.')
        
        wget.download(url, out = path)
        print('\n')
    
    def sbis_plugin_is_downloaded(self):
        current_dir = os.getcwd()

        downloaded_file_name = 'sbisplugin-setup-web.exe'
        downloaded_file_path = current_dir + '/' + downloaded_file_name

        assert os.path.isfile(downloaded_file_path)

        logger.info('Успешная загрузка плагина.')

    def plugin_size_is_correct(self):
        current_dir = os.getcwd()

        downloaded_file_name = 'sbisplugin-setup-web.exe'
        downloaded_file_path = current_dir + '/' + downloaded_file_name

        true_file_size = 8.17

        downloaded_file_size = os.path.getsize(downloaded_file_path) / 1048576
        downloaded_file_size = round(downloaded_file_size, 2)

        assert downloaded_file_size == true_file_size

        logger.info('Скачанный плагин имеет верный размер.')
