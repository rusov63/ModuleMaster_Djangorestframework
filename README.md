# Дипломный проект от SkyPro. 
# Django-приложение “Образовательные модули”

#### Описание.<br> Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть:
- порядковый номер
- название
- описание

#### Задача. <br>При создании проекта нужно: <br>
- реализовать для модели (моделей) все методы CRUD
- Полностью покрыть автоматизированными юнит-тестами все модели, сериализаторы, виды.

#### Требуемый стэк
- Python 3.11, Docker, Django, PostgreSQL, ORM, MVT/MTV, FBV/CBV, Serliazers, Viewset/Generic, Tests, Git, Readme, PEP8, Swagger

----------------------------------------------------------------------------------------------------------------

# Для запуска проекта локально Вам потребуется:

### 1. Установите систему контроля версий GIT с учетом вашей OS.

- Windows:

		https://git-scm.com/download/win
- Unix: sudo apt update (обновление системы).

        sudo apt install git-all

- Убедиться что все установлено:
            
        git --version
        
### 2. Установите СУБД PostgresQL для работы с базой данных. Пароль для входа поставьте: 123456

- Windows:

		https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

### 3. Установите язык программирования Python 3.11 
		https://www.python.org/downloads/windows/

### 4. Создайте и скопируйте проект в директорию:

		git clone git@github.com:rusov63/Skypro.Graduation_project.git

### 5. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости:

- Windows:

		python -m venv venv
        
		venv\Scripts\activate
        
		pip install -r requirements.txt
- Unix:

		python3 -m venv venv
        
        source venv/bin/activate
        
        pip install -r requirements.txt

### 6. Для работы с переменными окружения (базой данных) необходимо заполнить файл. Переменные настроены по умолчанию.

- .env.examples. 

### 7. Проведите миграции 

		python manage.py migrate

### 8. Для заполнения моделей данными необходимо выполнить следующую команду:

		python manage.py fill


### 9. Для запуска проекта:

- Windows:

		python manage.py runserver
	Если не прогружаются статические файлы

		python manage.py runserver --insecure 


##### Для создания административной панели:

		python manage.py createsuperuser
##### Для входа в административную панель
 
		http://127.0.0.1:8000/admin/

##### Создан и описан в корне проекта: Dockerfile, docker-compose.yaml. Запуск проекта одной командой

		docker-compose up -d --build

##### Открываем проект

		localhost:8000
        

## Документация проекта: 

		http://127.0.0.1:8000/swagger/
        
________________________________________________________________________________________________________________

#### В проекте используется Unittest

		python manage.py test

#### Для подсчета покрытия тестами использовался специальный пакет Coverage

		coverage run --source='.' manage.py test

		coverage report

![img_3.png](screen%2Fimg_3.png)

![img.png](screen%2Fimg.png)