
1.)))Создать виртуальное окружение 
			python3 -m venv <venv>
		
2.)))Устанавливаем нужные библиотеки и джанго 
			pip install <library>
			pip freeze > requirements.txt

3.)))Создание проекта и файла manage.py-это файл дает доступ командам
			django-admin startproject <name> .

4.)))Создание приложения для проекта
			python3 manage.py startapp <name>
			django-admin startapp <name>

5.)))Записать название вашего приложения в installed apps в настройках
			(подключения вашего приложение в проект)

6.)))Настройка базы данных
			настройка DATABASES = {
				'default':{
					'ENGINE':'django.db.backend.postgresql',
					'NAME':<name_of_your_db>,
					'USER':<hello>,
					'PASSWORD':<1>,
					'HOST':'localhost',
					'PORT':5432
					  }
					}
					
7.)))Создание базы данных в постгресс

8.)))Работа с миграциями:
			1)Создаем файл миграции
				python3 manage.py makemigrations
			2)Запускаем файл миграции
				python3 manage.py migrate
			
9.)))Запуск сервера
	python3 manage.py runserver

10.)))Создание суперюзера
	python3 manage.py createsuperuser
