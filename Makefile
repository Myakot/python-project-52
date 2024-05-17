install:
	poetry install #render.com doesn't see this for some reason and can't build? REMEMBER TO FIX LATER!!!!!!!!!

lint:
	poetry run flake8 task_manager

test:
	#poetry run pytest --cov=task_manager
	poetry run python3 manage.py test

test-coverage:
	#poetry run pytest --cov=task_manager --cov-report xml
	poetry run coverage run manage.py test
	poetry run coverage report
	poetry run coverage xml

build:
	./build.sh

selfcheck:
	poetry check

check: selfcheck test test-coverage lint

dev:
	poetry run python manage.py runserver

start:
	poetry run gunicorn task_manager.wsgi
