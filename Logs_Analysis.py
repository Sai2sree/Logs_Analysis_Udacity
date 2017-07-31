#!/usr/bin/env python3


import psycopg2
from datetime import datetime

DBNAME = "news"


def execute_query(query):
    """execute_query takes an SQL query as a parameter.
    Executes the query and returns the results as a list of tuples.
    args:
           query - an SQL query statement to be executed.
    returns:
           A list of tuples containing the results of the query.
    """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def question1():
    """Returns the most popular three articles of all time."""
    query = """SELECT articles.title,
            COUNT(*) as view
            FROM articles JOIN log
            ON log.path LIKE '%' ||articles.slug
            GROUP BY articles.title ORDER BY view DESC limit 3;"""
    articles = execute_query(query)
    print("\nThe most popular articles of all time are:\n")
    for title, views in articles:
        # Prints the most popular three articles of all time.
        print(("{} - {} views\n\n").format(title, views))


def question2():
    """Returns the most popular article authors of all time."""
    query = """SELECT authors.name, COUNT(*) as view
            FROM authors JOIN articles
            ON authors.id = articles.author
            JOIN log ON log.path LIKE '%' ||articles.slug
            GROUP BY authors.name ORDER BY view DESC;"""
    authors = execute_query(query)
    print("\nThe most popular article authors of all time are:\n")
    for author_name, views in authors:
        # Prints the most popular article authors of all time.
        print(("{} - {} views\n\n").format(author_name, views))


def question3():
    """Returns the days on which, more than 1% of requests lead to errors."""
    query = """WITH errors AS (
            SELECT time::date AS date,
            COUNT(time) AS sum
            FROM log WHERE status != '200 OK'
            GROUP BY date),
            total AS (
            SELECT time::date AS date,
            COUNT(time) AS all
            FROM log
            GROUP BY date)
            SELECT errors.date as date,
            CAST(100*errors.sum AS float)/ total.all
            FROM errors, total
            WHERE errors.date = total.date AND
            CAST(100*errors.sum AS float)/ total.all > 1;"""
    errors = execute_query(query)
    print("\nMore than 1% of requests lead to errors on:\n")
    for date, err_percent in errors:
        # Prints the days on which, more than 1% of requests lead to errors.
        print(("{0:%B %d, %Y} - {1:.2f} % errors").format(date, err_percent))


if __name__ == '__main__':
    """Calling all the three functions defined above."""
    question1()
    question2()
    question3()
