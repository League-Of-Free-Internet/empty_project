# empty_project

<div align="center">
<!-- Title: -->
  <a href="https://github.com/League-Of-Free-Internet">
    <img src="https://avatars.githubusercontent.com/u/156543782?s=400&u=7125039f153801ba2b620fd12b655afd690cb7aa&v=4" height="250">
  </a>
  <h1><a href="https://streetrussia.ru/">Улицы России</a> - начинаются с тебя</h1>
<!-- Labels: -->
  <!-- First row: -->
  <a href="https://github.com/League-Of-Free-Internet/empty_project">
    <img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Forbidden&color=cc0000&style=flat-square" height="20" alt="Contributions Forbidden">
  </a>
  <img src="https://pypi-camo.freetls.fastly.net/18c2771271928b1071e8d436680f9a0abf272294/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646a616e676f726573746672616d65776f726b2e737667?style=flat-square" height="20">
  <img src="https://img.shields.io/github/repo-size/League-Of-Free-Internet/empty_project?style=flat-square" height="20">
  <a href="https://img.shields.io/github/license/League-Of-Free-Internet/empty_project">
    <img src="https://img.shields.io/github/license/League-Of-Free-Internet/empty_project?style=flat-square" height="20" alt="license">
  </a>
  <!-- Second row: -->
  <br>
  <a href="https://github.com/League-Of-Free-Internet/empty_project/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/League-Of-Free-Internet/empty_project/codestyle_pep8.yml?branch=dev&label=Code Style&logo=github&style=flat-square" height="20" alt="GitHub Workflow Status">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" height="20" alt="pre-commit">
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-square" height="20" alt="code style: black">
  </a>
<!-- Short description: -->
  <h2>Best of the best project</h2>
</div>

> На стадии разработки.

Улицы России это проект единственной общероссийской организации в такой сфере, которая способствует
развитию уличных культур: воркаут, паркур, граффити, хип хоп и другие.
Улицы России ломают стереотипы о том, что это агрессивный и травмоопасный спорт
И доказывают, что этим может заниматься любой.

## Документация для работы в команде над проектом

[![Code Style](https://img.shields.io/badge/Прочитать-Документацию_Code_Style-blue?style=for-the-badge)](https://github.com//League-Of-Free-Internet/empty_project/blob/dev/.github/docs/code_style_rules.md) [![Pull Request](https://img.shields.io/badge/Прочитать-Документацию_Pull_Request-2ea44f?style=for-the-badge)](https://github.com/League-Of-Free-Internet/empty_project/blob/dev/.github/docs/pull_request_rules.md)

## Ссылка на проект
[![Site](https://img.shields.io/badge/Перейти_на-Сайт-2ea44f?style=for-the-badge)]()

## Технологии
- Python
- Django Rest Framework
- Djoser
- Simple JWT
- drf-yasg
- phonenumberslite

### Общая структура проекта:
```
├──.github/                 # Файлы и настройки, связанные с GitHub/Github actions
├──infra/                   # Директория с docker compose
├──requrements/             # Директория с файлами зависимостей
│   ├── develop.txt         # Файл со списком зависимостей для разработки
│   └── production.txt      # Файл со списком зависимостей для продуктовой версии
├── src/                    # Backend приложения Django/DRF
│   ├── about/              # Приложение для моделей об организации и документов [в разработке]
│   ├── api/                # API - программный интерфейс приложения [в разработке]
│   ├── config/             # Главная директория проекта с основными настройками [в разработке]
│   ├── core/               # Приложение общего назначения для вспомогательных функций, процессоров, констант [в разработке]
│   ├── disciplines/        # Приложение для моделей дисциплин и спорта [в разработке]
│   ├── events/             # Приложение для моделей о событиях и календаря [в разработке]
│   ├── news/               # Приложение для моделей новостной рубрики [в разработке]
│   ├── news/               # Приложение для моделей пользователей и участников проекта [в разработке]
│   ├──.dockerignore        # Конфигурационный файл, исключения Docker [в разработке]
│   ├──Dockerfile           # Конфигурационный файл Docker [в разработке]
│   └── manage.py           # Исполняемый файл
├── .env.example            # Файл примера для секретных переменных
├── .gitignore              # Файл со списком неотслеживаемых файлов и каталогов
├── .pre-commit-config.yaml # Файл настройки pre-commit
├── LICENSE                 # Лицензия проекта
└── setup.cfg               # Конфигурационный файл
```
## Установка для разработки локальный запуск:

- Клонируйте проект на свой компьютер:
```
git@github.com:League-Of-Free-Internet/empty_project.git
```
- Установите и активируйте виртуальное окружение c Python 3.12.3
```
cd ./empty_project/ &&
py -m venv venv
```
Для Windows:
```
source venv/Scripts/Activate
```
Для Linux
```
source venv/bin/activate
```
- Установите зависимости из файла requirements/develop.txt

Для Windows:
```
python -m pip install --upgrade pip
pip install -r requirements/develop.txt
```
для Linux:
```
pip install --upgrade pip
pip install -r requirements.txt
```
- Создайте переменные окружения в основной папке проекта "empty_project"
```
touch .env
```
- Добавьте ваши данные в файл .env
```
SECRET_KEY="Секретный код Django"
DEBUG=True
[Подробнее в файле .env.example]
```

## Проект разрабатывали:

| <!-- --> | <!-- -->      | <!-- -->    |
|----------|---------------|-------------|
| Владимир Васильев | Python-разработчик | [Cтраница GitHub](https://github.com/chem1sto) |
| Эдуард Гумен | Python-разработчик | [Cтраница GitHub](https://github.com/hydrospirt) |

## Лицензия

Пожалуйста, ознакомьтесь с [MIT license](https://github.com/League-Of-Free-Internet/empty_project?tab=MIT-1-ov-file)
