### YaCut

### Описание:
Проект YaCut — это сервис укорачивания ссылок. 
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками
- переадресация на исходный адрес при обращении к коротким ссылкам

### Инструкция по запуску:
**Клонируйте репозиторий:**
```
git clone git@github.com:VadimVolkovsky/yacut.git
```

**Установите и активируйте виртуальное окружение:**
для MacOS:
```
py -3.9 -m venv venv
```

для Windows:
```
py -3.9 -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```
**Установите зависимости из файла requirements.txt:**
```
pip install -r requirements.txt
```

**Из корневой директории запустите приложение:**
```
flask run
```


### Отправка запросов:

Приложение имеет удобный пользовательский интерфейс, по умолчанию доступный по адресу:

```
http://127.0.0.1:5000/
```

Пример запросов через API:

Method: POST (Создание короткой ссылки)
```
http://127.0.0.1:5000/api/id/
```
Body: 
```
{
    "url": "https://career.habr.com/vacancies/1000113868",
    "custom_id": ""
}
```

Response:
```
{
    "short_link": "http://127.0.0.1:5000/299504",
    "url": "https://career.habr.com/vacancies/1000113868"
}
```

Method: GET (Получение исходной ссылки по ID короткой ссылки)
```
http://127.0.0.1:5000/api/id/<short_link>/
```
Response:
```
{
    "url": "https://career.habr.com/vacancies/1000113868"
}
```


### Технологии:
- Python 3.9
- Flask


**Автор проекта:**

Vadim Volkovsky
