#!/usr/bin/env python3


import psycopg2
from datetime import datetime

DBNAME = "news"


def question1():
    """Returns the most popular three articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT articles.title, "
              "COUNT(*) as view "
              "FROM articles JOIN log "
              "ON log.path LIKE '%' ||articles.slug|| '%' "
              "GROUP BY articles.title ORDER BY view DESC limit 3;")
    articles = c.fetchall()
    print("\nThe most popular articles of all time are:\n")
    for article in articles:
        # Prints the most popular three articles of all time.
        print(("{} - {} views").format(article[0], article[1]))
    print("\n")
    db.close()


def question2():
    """Returns the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT authors.name, COUNT(*) as view "
              "FROM authors JOIN articles "
              "ON authors.id = articles.author "
              "JOIN log ON log.path LIKE '%' ||articles.slug|| '%' "
              "GROUP BY authors.name ORDER BY view DESC;")
    authors = c.fetchall()
    print("The most popular article authors of all time are:\n")
    for author in authors:
        # Prints the most popular article authors of all time.
        print(("{} - {} views").format(author[0], author[1]))
    print("\n")
    db.close()


def question3():
    """Returns the days on which, more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("WITH errors AS ( "
              "SELECT time::date AS date, "
              "COUNT(time) AS sum "
              "FROM log WHERE status != '200 OK' "
              "GROUP BY date), "
              "total AS ( "
              "SELECT time::date AS date, "
              "COUNT(time) AS all "
              "FROM log "
              " GROUP BY date) "
              "SELECT errors.date as date, "
              "CAST(100*errors.sum AS float)/ total.all "
              "FROM errors, total "
              "WHERE errors.date = total.date AND "
              "CAST(100*errors.sum AS float)/ total.all > 1;")
    errors = c.fetchall()
    print("More than 1% of requests lead to errors on:\n")
    # Converting date from 'YYYY-MM-DD' format to 'Month DD, YYYY' format.
    d = datetime.strftime(errors[0][0], '%B %d, %Y')
    # Prints the days on which, more than 1% of requests lead to errors.
    print(("{} - {} % errors\n").format(d, round(errors[0][1], 2)))
    db.close()

"""Calling all the three functions defined above."""
question1()
question2()
question3()
