#  Пульт охраны банка
### Описание
Модуль для отслеживания сотрудников банка, используюшие электронные пропуски, модуль может отображать список активных <br>
пропусков, отображает все визиты и длительность пребывания в хранилище по выбранному пропуску, также отображает есть ли <br>
подозрительные пребывания в хранилище (превышаюшие по времени более 60 минут).
### Технологии
Python 3.10,
Django 3.2
### Установка и запуск
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Добавьте в папку с проектом файл ".env" и внесите следующие данные:
```
DATABASE_ENGINE='движок базы данных'
DATABASE_HOST='хост'
DATABASE_PORT=='порт'
DATABASE_NAME='имя базы'
DATABASE_PASSWORD='пароль'
DATABASE_USER='имя пользователя'
SECRET_KEY='секретный ключ'
```    
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
- Пример запуска:
![img_2.png](img_2.png)


### Авторы
dvmn.org и подопытный
