from flask import render_template,redirect,url_for,request
from application import app
from application.forms import ReadingGenerator

import requests

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    response= requests.get("http://readings:5003").text
    response2 = requests.post("http://crystals:5001/").text
    response3 = requests.post("http://cards:5002/").text
    return render_template( "home.html", title = "Tarot Reading with Crystals", crystal=response2, card=response3, readings=response)

