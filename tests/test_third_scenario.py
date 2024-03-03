"""
Третий тестовый сценарий

1. Перейти на https://sbis.ru/
2. Перейти в раздел "Скачать СБИС"
3. Перейти на вкладку "СБИС Плагин"
4. Скачать плагин по ссылке
5. Убедиться, что плагин скачался
6. Убедиться, что плагин имеет верный размер
"""

from pages.sbis_home_page import SbisHomePage


def test_third_scenario(driver):

    sbis_home_page = SbisHomePage(driver)

    sbis_download_page = sbis_home_page.go_to_download_sbis()

    sbis_download_page.click_sbis_plugin_tab()

    sbis_download_page.download_sbis_plugin()

    sbis_download_page.sbis_plugin_is_downloaded()

    sbis_download_page.plugin_size_is_correct()
