# DjangoRestApi
REST Api built in Django. Also using Google Maps API for fun.

## Getting Started

Base Project to Build new REST API with Python and Django

### Prerequisites

To Install all required dependencies:
Windows:	python -m pip install -r requirements.txt
Unix:		pip install -r requirements.txt


If someone fails (DB Drivers) on linux, run:
sudo apt-get install libpq-dev python-dev

Installing DB Drivers (or other package) individually:
POSTGRES:	pip install psycopg2
MYSQL:      pip install mysql-python


TO RUN SERVER (FIRST TIME):
python manage.py migrate			(Creates Database)
python manage.py createsuperuser	(Creates a Superuser)
python manage.py runserver			(Run Server)


Notes:
Windows:  	python -m pip <command> <args> 
Unix:		pip <command> <args>


## Deployment

From scratch:
Gunicorn + Nginx
Notes:	https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
