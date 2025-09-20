# SOAP API Autotests (учебный проект)

## Описание
Учебный проект для практики автоматизации тестирования SOAP API.  
Цель — научиться писать автотесты на SOAP-запросы и ответы, работать с WSDL/XSD и валидировать контракт.

## Стек
- Python + pytest + zeep (SOAP client)
- lxml (валидация XML)
- allure (отчёты)

## Структура
- `tests/` — автотесты
- `samples/` — примеры SOAP-запросов и ответов (`.xml`)
- `docs/` — контракты (`.wsdl`, `.xsd`)

## Запуск
```bash
pytest -q --alluredir=reports/allure
allure serve reports/allure
