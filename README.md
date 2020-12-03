# Django Simple Todo API with Firebase Firestore Database

This is simple todo API created using Django and Django Rest Framework.
This project showcases the implementation of Firebase Firestore Database with Django.


## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.8
+ Git
+ pip
+ Virtualenv / virtualenvwrapper

## Requirements

+ Django==3.1.3
+ firebase-admin==4.4.0
+ djangorestframework==3.12.2

## Project Installation

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),
```bash
mkvirtualenv {{project_name}}   # create and activate environment
workon {{project_name}}   # reactivate existing environment
```

Clone GitHub Project,
```bash
git clone git@github.com:saadmk11/django-todo.git

cd django-todo
```

Create ``.env`` file in the ``django-todo`` directory and add the firebase secret (.json) file path to it. 
Example:
```bash
FIREBASE_ADMIN_CERT=firebase-secret.json
```
Install development dependencies,
```bash
pip install -r requirements.txt
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```
