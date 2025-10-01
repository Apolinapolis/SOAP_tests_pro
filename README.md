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
Установить зависимости
pip install -r requirements.txt  

Запустить тесты
pytest -q --alluredir=reports/allure  

Сформировать и открыть отчёт Allure
allure serve reports/allure
