## Getting Started

A REST api written in Django

## Technologies used
Python: Python 3.9.7
Django: Django==4.2.10
DRF: A powerful and flexible toolkit for building APIs. djangorestframework==3.14.0

## Installation
If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you have to download python3.

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    $ pip3 install virtualenv


## Dependencies
1. Cd into your project as such:
    $ cd test123

2. Create & Activate virtualen:
    $ python3 -m venv env
    $ source env/bin/activate

3. After Activate virtualenv install the dependencies needed to run the app
    $ pip3 install -r requirements.txt


## Run It

Fire up the server using this one simple command:
    $ python3 manage.py runserver

You can now access the file api service on your browser by using
    http://localhost:8000/blog/
