# OJS API

> Python/Django API for OJS.

## Project

This project is a tool for
* OJS instance :
    * to **expose** its Journals metadata and files through an API accessible to any service registered
    * to **register** these distant consumer services to grant them access to the API
* consumer service :
    * to **retrieve** Journals metadata and files from any OJS instance where it is registered

## OJS versions supported

* 2.4.8

## Installation

### Clone the project

Make sure to clone locally the project from the origin git repository.

    $ git clone git@github.com:erudit/pkp-ojs-api.git

### Python 3 environment

This project runs with Python 3. You can get a Python 3 environment if you
[download an Anaconda Python distribution][anaconda].

We recommend to have a dedicated Python virtual environment to install the
project's Python dependencies. You can do so with your Anaconda Python distribution,
installing IPython package in a new environment called 'ojs':

    $ conda create --name ojs ipython

Once the environment is created, you need to activate it in order to use it or
develop in it.

    $ source activate ojs

The environment is activated when your command line prompt is prefixed with
your environment name.

    (ojs)$

If you're done using or developing in your environment, you can deactivate it.

    (ojs)$ source deactivate

### Dependencies

This project is built with Django, a Python web development framework. It relies
also on other Python packages.

To install dependencies, make sure that
* you are in the project's root directory
* your environment is activated

    $ cd /path/to/pkp-ojs-api
    $ source activate ojs

You can then install the Python requirements declared in the
`requirements.txt` file using pip.

    (ojs)$ pip install -r requirements.txt

### Settings

Create a `settings_env.py` file in the cjoe folder, right aside the `settings.py` file.

You can override all settings of the `settings.py` file in `settings_env.py` so
that the settings are appropriate for your environment (dev, test, prod...).

## Development

Make sure you have a complete installation and that your environment is activated.

Edit the `settings_env.py` file with your development settings.

You can launch Django's development server...

    (ojs)$ python manage.py runserver

... or interactively experiment with the code in IPython

    (ojs)$ python manage.py shell

## OJS instance usage

An OJS instance may choose to expose its Journals metadata and files to a registered distant consumer service. To do so, it has to
* install this tool (see previous section)
* expose API
* register services

### Expose API

### Register a service

## Consumer service usage

A consumer service registered with an OJS instance can have access to its Journals metadata and files. To do so, it has to
* install this tool (see previous section)
* configure access to OJS instance API
* call an OJS instance API

### Configure access to OJS instance API

### Call an OJS instance API

## License

This program is release under the GNU GPLv3 license. A copy of this license is
available in the file [LICENSE][license].

[license]: ./LICENSE
