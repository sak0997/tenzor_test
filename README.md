# Тестовое задание для компании Тензор. Вакансия: программист-тестировщик (отдел автотестирования)

Правила выполнения задания:

  1. Необходимо автоматизировать проверки двух обязательных
     сценариев.
  
  2. Третий сценарий выполнять не обязательно, но это будет
     дополнительным плюсом на техническом собеседовании.
  
  3. Автотесты реализованы на Python 3 и Selenium Webdriver
  
  4. В качестве тестового framework используется pytest
  
  5. Реализован паттерн PageObject
     
  6. Приветствуются любые сторонние библиотеки для логирования,
     отчетов, selenium wrapper

  7. Готовый проект залит на github/gitlab без кешей, драйверов и
     виртуальных окружений. С открытым доступом на чтение.

`pages` содержит описание классов страниц. Класс `BasePage` содержит базовую функциональность для всех страниц, остальные классы страниц наследуются от `BasePage`.

```
- SbisHomePage - домашняя страница sbis.ru
- SbisContactsPage - раздел Контакты sbis.ru
- SbisDownloadPage - раздел Скачать sbis.ru
- TensorHomePage - домашняя страница tensor.ru
- TensorAboutPage - раздел О компании tensor.ru
```

`tests` содержит сценарии тестирования.

#### Запустить все тесты можно следующей командой: 
```sh
python -m pytest --capture=no tests
```
