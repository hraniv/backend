# Hraniv API

API back-end built with Python

### Core technologies:
* Python 3.5
* Falcon
* Django 1.10 (ORM and admin panel)
* PostgreSQL

### Development
To run application for development use following command:

`gunicorn --reload  --timeout 999 app:api`

*Note: DJANGO_SETTINGS_MODULE environment variable must be set* 
