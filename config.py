import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "youllneverguess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root@localhost/icc?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LINES_PER_PAGE = 30
    ANNO_UP_FACTOR = 10
    ANNO_DOWN_FACTOR = 15
    AUTHORIZATION = { 'EDIT_QUEUE' : 10 }
