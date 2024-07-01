import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') or 'postgresql://postgres:password@localhost/postgres' #'postgresql://username:password@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
