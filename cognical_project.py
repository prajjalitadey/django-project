# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:36:35 2016

@author: prajjalitadey
"""

import pandas as pd
import psycopg2 as pg
import time, datetime
import csv


# ---*----- Create Database ------*-

#connection = pg.connect(database='postgres', user='postgres', host = 'localhost', password='greenkey217')
#
#connection.set_isolation_level(0)
#cur = connection.cursor()
#cur.execute("CREATE DATABASE ml_latest")
#connection.commit()
#
#cur.close()
#connection.close()




# ---*----- Connect to Database ------*---

#connection = pg.connect(database='ml_latest', user='postgres', host = 'localhost', password='greenkey217')
#cur = connection.cursor()



# ---*----- Create Tables ------*---

#cur.execute("CREATE TABLE movies(movieid INT, title VARCHAR(150), genres VARCHAR(200));")
#cur.execute("CREATE TABLE links(movieid INT, imdb_id INT, tmdb_id INT);")
#cur.execute("CREATE TABLE ratings(userid INT, movieid INT, rating FLOAT, timestamp TIMESTAMP);")
#cur.execute("CREATE TABLE tags(userid INT, movieid INT, tag VARCHAR(300), timestamp TIMESTAMP);")



# ---*----- Alter Primary Keys ------*---

#cur.execute("ALTER TABLE movies ADD CONSTRAINT mpk PRIMARY KEY(movieid);")
#cur.execute("ALTER TABLE links ADD CONSTRAINT lpk PRIMARY KEY(movieid);")
#cur.execute("ALTER TABLE ratings ADD CONSTRAINT rpk PRIMARY KEY(userid, movieid);")
#cur.execute("ALTER TABLE tags ADD CONSTRAINT tpk PRIMARY KEY(userid, movieid, tag);")



# ---*----- Copy CSV files into PostgreSQL ------*---

#cur.execute("COPY movies FROM '/Users/prajjalitadey/ml-latest-small/movies.csv' DELIMITER ',' CSV HEADER;")
#cur.execute("COPY links FROM '/Users/prajjalitadey/ml-latest-small/links.csv' DELIMITER ',' CSV HEADER;")

#with open('/Users/prajjalitadey/ml-latest-small/ratings.csv', 'rb') as ratingsfile:
#    reader = csv.reader(ratingsfile, delimiter=',')
#    for row in reader:
#        if reader.line_num > 1:
#            user = int(row[0])
#            movie = int(row[1])
#            rating = float(row[2])
#            timestamp = datetime.datetime.utcfromtimestamp(int(row[3]))
#            cur.execute("INSERT INTO ratings VALUES (%s, %s, %s, %s);", (user, movie, rating, timestamp))

#with open('/Users/prajjalitadey/ml-latest-small/tags.csv', 'rb') as tagsfile:
#    reader = csv.reader(tagsfile, delimiter=',')
#    for row in reader:
#        if reader.line_num > 1:
#            user = int(row[0])
#            movie = int(row[1])
#            tag = row[2]
#            timestamp = datetime.datetime.utcfromtimestamp(int(row[3]))
#            cur.execute("INSERT INTO tags VALUES (%s, %s, %s, %s);", (user, movie, tag, timestamp))


#connection.commit()
#
#cur.close()
#connection.close()


# ---*-------------------- After Creating Models ----------------------*---

connection = pg.connect(database='ml_latest', user='postgres', host = 'localhost', password='greenkey217')
cur = connection.cursor()

with open('/Users/prajjalitadey/ml-latest-small/movies.csv', 'rb') as moviesfile:
    reader = csv.reader(moviesfile, delimiter=',')
    for row in reader:
        if reader.line_num > 1:
            movie = int(row[0])
            title = row[1]
            genres = row[2]
            cur.execute("INSERT INTO ml_latest_movies (movieid, title, genres) VALUES (%s, %s, %s);", (movie, title, genres))


with open('/Users/prajjalitadey/ml-latest-small/links.csv', 'rb') as linksfile:
    reader = csv.reader(linksfile, delimiter=',')
    for row in reader:
        if reader.line_num > 1:
            try:
                movie = int(row[0])
                imdb_id = int(row[1])
                tmdb_id = int(row[2])
                cur.execute("INSERT INTO ml_latest_links (movieid, imdb_id, tmdb_id) VALUES (%s, %s, %s);", (movie, imdb_id, tmdb_id))
            except ValueError:
                movie = int(row[0])
                imdb_id = int(row[1])
                cur.execute("INSERT INTO ml_latest_links (movieid, imdb_id, tmdb_id) VALUES (%s, %s, %s);", (movie, imdb_id, None))



with open('/Users/prajjalitadey/ml-latest-small/ratings.csv', 'rb') as ratingsfile:
    reader = csv.reader(ratingsfile, delimiter=',')
    for row in reader:
        if reader.line_num > 1:
            user = int(row[0])
            movie = int(row[1])
            rating = float(row[2])
            timestamp = datetime.datetime.utcfromtimestamp(int(row[3]))
            cur.execute("INSERT INTO ml_latest_ratings (userid, movieid, rating, timestamp) VALUES (%s, %s, %s, %s);", (user, movie, rating, timestamp))


with open('/Users/prajjalitadey/ml-latest-small/tags.csv', 'rb') as tagsfile:
    reader = csv.reader(tagsfile, delimiter=',')
    for row in reader:
        if reader.line_num > 1:
            user = int(row[0])
            movie = int(row[1])
            tag = row[2]
            timestamp = datetime.datetime.utcfromtimestamp(int(row[3]))
            cur.execute("INSERT INTO ml_latest_tags (userid, movieid, tag, timestamp) VALUES (%s, %s, %s, %s);", (user, movie, tag, timestamp))


connection.commit()
cur.close()
connection.close()
