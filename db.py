import sqlite3, os
from flask import g
import psycopg2
from urllib import parse

def get_db():
    # Once a connection is established you can use the cursor object to iterate over a list
    # or access a value directly using its key. The link below shows an example using the dictionary cursor extra
    # https://www.psycopg.org/docs/extras.html
    db = getattr(g, '_database', None)
    if db is None:
        flask_env = os.getenv('FLASK_ENV', default='development')
        if flask_env == 'production':
            # documentation for setting up psycopg2
            # https://developer.salesforce.com/blogs/developer-relations/2016/05/heroku-connect-flask-psycopg2.html
            DATABASE = os.getenv('DATABASE_URL')
            url = parse.urlparse(DATABASE)
            db_connect = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
            db = psycopg2.connect(db_connect, cursor_factory=psycopg2.extras.DictCursor)
        else:
            # It is recommended to set a default for the DATABASE_URL in case the students do not have postgres installed on their machines
            # Example: default='postgres://root:password@localhost:5432/databasename'
            DATABASE = os.getenv('DATABASE_URL')
            # Example Database url below
            # DATABASE_URL "postgres://{username}:{password}@localhost:5432/{database}"
            url = parse.urlparse(DATABASE)
            db_connect = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
            db = psycopg2.connect(db_connect, cursor_factory=psycopg2.extras.DictCursor)
            g._database = db
    return db