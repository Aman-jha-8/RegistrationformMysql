# RegistrationformMysql
pip install django
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'your_db_name',
		'USER': 'root',
		'PASSWORD': 'paswd_of_db',
		'HOST':'localhost',
		'PORT':'3306',
	}
}
python manage.py makemigration firstproject
python manage.py migrate
python manage.py runserver
