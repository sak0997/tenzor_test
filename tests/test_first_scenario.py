"""
Первый тестовый сценарий

1. Перейти на сайт sbis.ru в раздел "Контакты"
2. Найти баннер "Тензор" и кликнуть по нему
3. Перейти на https://tensor.ru/
4. Проверить, что есть блок "Сила в людях"
5. Перейти в блоке "Сила в людях" в "Подробнее" и убедиться, что открывается https://tensor.ru/about
6. Найти раздел "Работаем" и проверить, что у всех фотографий хронологии одинаковые высота (height) и ширина (width)
"""

from pages.sbis_home_page import SbisHomePage


def test_first_scenario(driver):

    sbis_home_page = SbisHomePage(driver)
    
    sbis_contacts_page = sbis_home_page.go_to_contacts_page()

    tensor_home_page = sbis_contacts_page.click_tensor_banner()

    tensor_home_page.url_is_valid()

    tensor_home_page.people_strength_block_is_presented()

    tensor_about_page = tensor_home_page.go_to_tensor_about()

    tensor_about_page.url_is_valid()

    tensor_about_page.all_photos_are_the_same_size()
