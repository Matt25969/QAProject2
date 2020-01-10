import os, pymysql
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = os.getenv('MY_SQL_USER')
password = os.getenv('MY_SQL_PASSWORD')
url = os.getenv('MY_SQL_URL')
db = os.getenv('MY_SQL_DATABASE')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(user, password, url, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db=SQLAlchemy(app)



from application import routes
