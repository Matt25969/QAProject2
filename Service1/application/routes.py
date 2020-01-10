from flask import render_template,redirect,url_for,request
from application import app
from application.forms import ReadingGenerator

import requests

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    getreading = ReadingGenerator()

    if request.method == "GET":
        reading = { "crystal" : "",
                    "card" : "",
                    "meaning" : "" }
    if ReadingGenerator.is_submitted():
        response = requests.get("http://readings:5004")

    return tender_template( "home.html", title = "Tarot Reading with Crystals")

