# SOAP API Autotests (учебный проект)

## Описание
Учебный проект для практики автоматизации тестирования SOAP API.  
Цель — научиться писать автотесты на SOAP-запросы и ответы, работать с WSDL/XSD и валидировать контракт.

## Стек
- Python + pytest + Jinja2 (шаблонизатор)
- xmlschema (валидация XML)
- allure (отчёты)

## Структура
- `tests/soap` — автотесты
- `tests/conftest.py` — фикстуры pytest
- `templates/` — примеры SOAP-запросов и ответов (`.xml`, `.xsd`)

## Запуск
- pip install -r requirements.txt  (установить зависимости)
- pytest -q --alluredir=reports/allure (запустить тесты)
- allure serve reports/allure (сфирмировать отчет)
