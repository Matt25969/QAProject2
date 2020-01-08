import os, pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')
host=os.getenv('MYSQL_HOST')
db=os.getenv('DATABASE')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(user, password, host, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db=SQLAlchemy()

from application import routes
