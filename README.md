# Logs_Analysis_Udacity
An internal reporting tool for a newpaper site to discover what kind of articles the site's readers like, by exploring site's database.

## Introduction

This project is a python program that uses psycopg2 module to connect to a database. It explores a large database with over a million rows to draw business conclusions. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

### The database includes three tables:
* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.

### This project drives the following conclusions:
1. Most popular three articles of all time.
2. Most popular article authors of all time.
3. Days on which more than 1% of requests lead to errors.

## Instructions to run the code

### You will need:
* [Python3](https://www.python.org/downloads/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* 'newsdata.sql' file provided by Udacity.

### Setup

* Install [Python3](https://www.python.org/downloads/), [Vagrant](https://www.vagrantup.com/), and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
* Clone this repository.

### To Run

1. From your terminal, inside the vagrant subdirectory, run the command ``vagrant up``.
2. Once you got the shell prompt back, run the command ``vagrant ssh`` to log in to the Linux VM.
3. To load the data, use the command ``psql -d news -f newsdata.sql``.
4. To execute the program, run the command ``python Logs_Analysis.py`` from the command line.
