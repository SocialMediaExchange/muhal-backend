# muhal-backend
A new backend to Muhal.org-style websites

# Installation

For production purposes, you should use muhal-deployment (coming soon!). 

For development purposes, follow the steps below:

0. Setup a Python3.6 environment using [`pipenv`](https://pipenv.readthedocs.io/en/latest/).
1. Clone this repository, and run `pipenv install`. 
2. Create a `muhal-backend/muhal/muhal/local_settings.py` file, with the following contents:
```python
# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "<my very long random string here>"
NEVERCACHE_KEY = "<my different very long random string here>"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# Allowed development hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1"]
```
3. Run `python manage.py create.db` to create a database, superuser, and some (optional) stock content.
4. Run `python manage.py runserver` to launch the local server. 

