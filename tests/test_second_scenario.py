"""
Второй тестовый сценарий

1. Перейти на сайт sbis.ru в раздел Контакты
2. Проверить, что верно определился регион и есть список партнеров
3. Изменить регион на Камчатский край
4. Проверить, что регион был верно изменен, список партнеров изменился, url и title содержат информацию выбранного региона
"""

from pages.sbis_home_page import SbisHomePage


def test_second_scenario(driver):
    
    sbis_home_page = SbisHomePage(driver)

    sbis_contacts_page = sbis_home_page.go_to_contacts_page()

    sbis_contacts_page.region_defined_correct()

    sbis_contacts_page.partners_list_presented_and_visible()

    sbis_contacts_page.change_region()

    sbis_contacts_page.region_changed_successfully()

    sbis_contacts_page.partners_list_changed_successfully()

    sbis_contacts_page.url_is_correct()
    
    sbis_contacts_page.title_is_correct()
