# django_excel_csv

A simple and generic Django app to export csv from anywhere. 

Just extend one class and implement three methods, to use:
* get_column_names()
* get_data()


## Ajax
Ajax and regular browser request compatible


## Python 2 and Python 3
* Python 2.7 tested with Django 1.8
* Python 3.6 tested with Django 3.0



## Install 

**Add django_excel_csv to the requirements of your Django project**
* -e git+https://gitlab.com/bv_fapesp/django_excel_csv#egg=django_excel_csv

**Or directly install with pip**
* pip install git+https://gitlab.com/bv_fapesp/django_excel_csv#egg=django_excel_csv



## Before you use

You can inspect this app installing it outside your project. 


**Clone and run tests:**
*  git clone https://gitlab.com/bv_fapesp/django_excel_csv.git

**Install requirements**
*  pip install requirements.txt

**Run tests**
* python runtests.py


**Set database**

For default test_settings.py, database is set dummy, which raises an ImproperlyConfigured Error.
You can set your database engine (Postgres, MySQL, sqlite3...)
 

## CSV with Javascript
Use this snipet to deliver your CSV using Javascript


https://gitlab.com/bv_fapesp/django_excel_csv/snippets/1954292.js