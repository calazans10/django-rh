# rh_system

A simple rh system created to Sieve's challenge

## Usage

    git clone git@github.com:calazans10/rh_system.git
    cd rh_system

install virtualenv and virtualenvwrapper

    pip install virtualenv
    sudo pip install virtualenvwrapper

create virtualenvs folder

    mkdir ~/.virtualenvs

add to your "~/.bashrc"

    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

create virtualenv and install requirements

    mkvirtualenv env-rh-system
    pip install -r requirements.txt

install mysql

    sudo apt-get install python-mysqldb
    pip install MySQL-python

create database

    mysql -u root -p
    mysql> create database rh_system;
    mysql> crtl + d

sync and migrate database

    ./manage.py syncd
    ./manage.py --migrate

use project

    ./manage.py runserver 0.0.0.0:8000

