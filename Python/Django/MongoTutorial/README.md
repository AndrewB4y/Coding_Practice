# Mongo-Django project practice

Repository for the practice and study of a simple blog implementation using Django and MongoDB, this poject follows the tutorial found at [https://django-mongodb-engine.readthedocs.io/en/latest/tutorial.html](https://django-mongodb-engine.readthedocs.io/en/latest/tutorial.html) by May 2021.

## Virtualenv

For the creation and use of a virtual environment using "virtualenv":

### Instalation

`pip install virtualenv`

### Creation

`virtualenv django_mongo`

### To join the environment

On windows:

1. Check the ExecutionPolicy
   `Get-ExecutionPolicy`
   If the output is `Unrestricted` skip to step 2, if the output is `Restricted`run:`Set-ExecutionPolicy -ExecutionPolicy Unrestricted`
2. To run the environment
   `.\django_mongo\Scripts\activate`
   Here your prompt should be prefix-ed with (django_mongo)
3. To deactivate the environment
   `deactivate`

On Bash:

1. To run the environment
   `source django_mongo/bin/activate`
2. To deactivate the environment
   `deactivate`

## Django non-rel

Django non-rel is a project to support Django on non-relational ('NoSQL') databases.
Currently, we support [MongoDB](http://www.mongodb.org/) and [Google App Engine](https://developers.google.com/appengine/). (from [Django non-rel](https://django-nonrel.org/) page on May 2021)

### Installation

Installation of Django non-rel

`pip install git+https://github.com/django-nonrel/django@nonrel-1.5`

Installation of DjangoToolbox

`pip install git+https://github.com/django-nonrel/djangotoolbox`

Installation of Django MongoDB Engine

`pip install git+https://github.com/django-nonrel/mongodb-engine`
