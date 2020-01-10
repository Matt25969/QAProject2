from flask import render_template,redirect,url_for,request
from application import app
from application.forms import ReadingGenerator

import requests

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET','POST'])


def home():

    #if request.method == "GET":
    # reading = { "crystal" :"",
     #               "card" : "",
      #              "meaning" : "" }


    response = requests.get("http://readings:5003")
    text = response.text

    return render_template( "home.html", title = "Tarot Reading with Crystals", readings=text)

'''

def home():
    form = ReadingGenerator()
    if form.validate_on_submit():
        response = requests.get("http://readings:5004")
        reading = { "crystal" : "",
                    "card" : "",
                    "meaning" : "" }
     return tender_template( "home.html", title = "Tarot Reading with Crystals")
'''
