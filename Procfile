	
	release: python  manage.py makemigrations --noinput
	release: python  manage.py makemigrations accounts --noinput
	release: python  manage.py makemigrations main --noinput
	release: python  manage.py makemigrations schools --noinput
	release: python  manage.py makemigrations student --noinput
	release: python  manage.py makemigrations teacher --noinput
	release: python  manage.py migrate --noinput

	web: gunicorn bloggerq.wsgi

