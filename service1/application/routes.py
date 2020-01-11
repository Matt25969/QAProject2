from flask import render_template,redirect,url_for,request
from application import app
from application.forms import ReadingGenerator

import requests

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET','POST'])


def home():

    response = requests.post("http://readings:5003").text

    #text = response.text
    
    return render_template( "home.html", title = "Tarot Reading with Crystals", readings=response)

