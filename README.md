# Encyclopedia

Скрипт делает небольшой статический сайт-энциклопедию на основе статей в формате markdown.  
Сами статьи должны располагаться в папке articles, шаблоны для оформления - в папке templates, готовые html страницы будут размещены в папке static.  
Информация о статьях указывается в конфигурационном файле формата json, который подаётся на вход скрипту.


# Quickstart

Скрипт требует для своей работы установленный интерпретатор Python версии 3.5, а также некоторые дополнительные зависимости, которые можно установить следующим образом:
```
pip install -r requirements.txt
```

Запуск на Linux:

```#!bash
$ python site_generator.py config.json
```
Запуск на Windows происходит аналогично.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
