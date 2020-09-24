	
	release: python  manage.py makemigrations --noinput
	release: python  manage.py migrate --noinput
	release: python  manage.py runserver --noinput

	web: gunicorn bloggerq.wsgi

