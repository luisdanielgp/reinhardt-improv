# reinhardt
[![python](https://img.shields.io/badge/python-3.6-blue.svg "python 3.6")](https://docs.python.org/3/whatsnew/3.6.html)
[![django-version](https://img.shields.io/badge/django-2.0-blue.svg "django 2.0")](https://docs.djangoproject.com/en/2.0/releases/2.0/)

## Features

 - Docker containers:
   - reinhardt_postgres:
     - Database configured to `port 5432`
   - reinhardt_redis:
     - Configured to `port 6379`
   - reinhardt_django:
     - Python 3.6
     - Django 2.0
     - Postgres already configured
     - Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
     - Enhancements to Django's static file serving functionality via WhiteNoise.
 - Latest Python 3.6 runtime environment.

## Requirements
This project has the following requirements by default:

```
  dj-database-url==0.4.1
  Django==2.0
  gunicorn==19.6.0
  psycopg2==2.7.3.2
  whitenoise==3.2
```
- - -

# The Template
An utterly fantastic project starter template for Django 2.0.

## Features
 - Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
 - Enhancements to Django's static file serving functionality via WhiteNoise.
 - Latest Python 3.6 runtime environment.
 - This template creates a project with three docker containers:
    - A python 3.6 container where the Django project is found 2.0.
    - A postgres container.
    - A Redis container.

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Create a virtual environment with python 3.6 (`$ virtualenv -p python3 venv`)
3. Activate the virtual environment (`$ source venv/bin/activate`)
3. Install Django (`$ pip install django`)
4. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy:

    $ django-admin.py startproject --template=/[TEMPLATE-DIRECTORY]/heroku-docker-django-template-master.zip --name=Procfile,docker-compose.yml,README.md,wait-for-postgres.sh helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You **have** to replace ``[TEMPLATE-DIRECTORY]``  and you can replace ``helloworld`` with your desired project name.

## Customize .gitignore

This template has a file ready to work with django, python, redis, macOS, linux and vim. If you think you need something more you can add it as follows (if you have `gi` in the terminal):
```
$ gi django,macos,python >> .gitignore
```
Some of the things you can add are:
```
android
c
cvs
django
dotsettings
elixir
emacs
go
gradle
java
jetbrains
latex
linux
node
objective-c
pycharm
python
sass
vagrant
vim
virtualenv
windows
```

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.
