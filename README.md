# Diplom_autotests_python_yougil

## Шаблон для автоматизации тестирования на python
Система управления проектами: ru.yougile.com
Документация API: ru.yougile.com/api-v2
### Шаги
1. Склонировать проект git clone `https://github.com/fedorovai1964/Diplom_autotests_python_yougil.git`
2. Установить все зависимости pip install -r requirements.txt `pip freeze > requirements.txt`
3. Создать файл .env в корне по образцу .env.example и заполнить своими данными: URL, email, пароль, API-токен, project_id.
4. Запустить тесты `pytest -s -v` . Три режима запуска тестов через маркеры:
- `pytest -m -s -v "api"`   # только API-тесты
- `pytest -m -s -v "ui"`   # только UI-тесты
- `pytest -s -v`    # все тесты
5. Сгенерировать отчет `allure generate allure-files -o allure-report`
6. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- requests
- allure
- config
- webdriver-manager

### Структура:
- api/ — API-клиент (BoardApi)
- pages/ — Page Object (AuthPage, MainPage)
- test/api/ — API-тесты
- test/ui/ — UI-тесты
- conftest.py — фикстуры pytest
- .env — секреты (в .gitignore)
- pytest.ini — регистрация маркеров

 
### Тест-план и документация
Страница проекта в Yonote:[Yonote](https://irina-study-skypro.yonote.ru/share/2007df53-f558-4bf9-bad8-d6529f9ff73e)


### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/) 
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
