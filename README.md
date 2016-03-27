[![Coverage Status](https://coveralls.io/repos/github/akrv/flask-inventory/badge.svg?branch=master)](https://coveralls.io/github/akrv/flask-inventory?branch=master)
# Flask Inventory

Flask Inventory is an attempt to create an inventory management system for
a small business using the flask framework.  Currently the project is under heavy
development.  



## Quick Start

### Basics

1. Activate a virtualenv
1. Install the requirements

### Set Environment Variables

Update *config.py*, and then run:

```sh
$ export APP_SETTINGS="project.config.DevelopmentConfig"
```

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
