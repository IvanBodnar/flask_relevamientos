import os

SECRET_KEY = '\x9a\x01\xacR\xe6\xe7]\x06\x04\x1a\x00\x0bX\xa6i\xf2wG\x88\xb0\x9cu\xd6\xb7'
DEBUG = True
DB_USERNAME = 'ivan'
DB_PASSWORD = 'ivan'
DB_HOST = 'localhost'
RELEVAMIENTOS_DB_NAME = 'relevamientos'
DB_URI = 'postgresql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, RELEVAMIENTOS_DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
