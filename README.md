# Logs_Analysis_Udacity
An internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. This is done by exploring site's database which contains newspaper articles, as well as the web server log for the site.

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
* [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file provided by Udacity.

### Setup

* Install [Vagrant](https://www.vagrantup.com/), and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
* Clone this repository.

### To Run
1. Create a directory with Vagrantfile and [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) files in it and navigate to it. 
2. From your terminal, run the command ``vagrant up``. 
3. Once you got the shell prompt back, run the command ``vagrant ssh`` to log in to the Linux VM.
4. Run the command ``unzip newsdata.zip`` to unzip the newsdata.zip file
5. Use the command ``psql -d news -f newsdata.sql`` to load the data.
6. To execute the program, run the command ``python3 Logs_Analysis.py``.

## Output
```
• The most popular articles of all time are:

 * Candidate is jerk, alleges rival - 338647 views
 * Bears love berries, alleges bear - 253801 views
 * Bad things gone, say good people - 170098 views


• The most popular article authors of all time are:

 * Ursula La Multa - 507594 views
 * Rudolf von Treppenwitz - 423457 views
 * Anonymous Contributor - 170098 views
 * Markoff Chaney - 84557 views


• More than 1% of requests lead to errors on:

 * July 17, 2016 - 2.26 % errors

```
