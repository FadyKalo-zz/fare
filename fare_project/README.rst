============
Fare-Project
============

To use this project follow these steps:

#. A
#. B
#. C

*note: these instructions show ...*

Working Environment
===================

Let's put here the info about the environment.

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv --distribute fare

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

Virtualenv with virtualenvwrapper
------------------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you::

    $ mkdir fare
    $ mkvirtualenv -a fare fare-dev
    $ cd fare && add2virtualenv `pwd`

Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django


Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Yummly Doc
==========

Here we shuold add the Yummly documentation for this project

Run the Server
==============

Depending on where you are running the server:

In development::

    $ python manage.py runserver --settings=fare.settings.local

Settings are the following:

#. fare.settings.local: used for local development server.
#. fare.settings.staging: this is our pre-production server.
#. fare.settings.test: settings for the test server.
#. fare.settings.production: production setting for the live server.

If necessary we can add individual settings file for development such as `dev_fady.py`.

*note: IMPORTANT: keep in mind that every settings file needs a requirement file too.*

Acknowledgements
================

- Many thanks to us.
- and to us again, the contributors_ to this project.

.. _contributors: CONTRIBUTORS.txt
