# Yatube
### Описание
Этот проект создан в учебных целях. Представляет из себя мини социальную сеть или площадку для блогов. Так как тема изучения - API, из проекта убран WEB-интерфейс. Все действия только через API.
### Возможности
1. Аутентификация пользователя. 
2. Подписки на пользователей.
3. Просмотр, создание, изменение и удаление записей.
4. Группы. При создании записей можно указывать принадлежность к группе.
5. Пагинация.
6. Возможность добавления, редактирования, удаления своих комментариев и просмотр чужих.

### Технологии

Python 3.7

Django 2.2.16

Django Rest Framework 3.12.4

Simple JWT

SQLite3

### Запуск проекта

 - Клонируйте репозиторий:
```
git clone git@github.com:korecbtc/api_yatube.git
```
 - Перейдите в папку с проектом

 - Установите и активируйте виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

 - Установите зависимости из файла requirements.txt

``` 
pip install -r requirements.txt
```

- В папке с файлом manage.py выполните команды:

``` 
python manage.py migrate

python manage.py runserver 
```
### Примеры запросов

Получить список всех постов:  
``` GET /api/v1/posts/ ```  
Добавление нового поста:  
``` POST /api/v1/posts/ ```   
Получить список всех групп:  
``` GET /api/v1/groups/ ```  
Добавление нового комментария:  
``` POST /api/v1/posts/{post_id}/comments/ ```  
Удаление комментария по id:  
``` DELETE /api/v1/posts/{post_id}/comments/{id}/ ```  
Получение списока подписок:  
``` GET /api/v1/follow/ ```  
Подписка пользователя на пользователя переданного в запросе:  
``` POST /api/v1/follow/ ```  

Полный список запросов можно посмотреть в документации после запуска проекта по адресу:
http://127.0.0.1:8000/redoc/

### Автор
Иван Корец
