from flask import render_template, redirect, url_for
from application import app
import requests

@app.route("/", methods= ["GET", "POST"])
def reading():
    crystal=requests.get("http://crystals:5001").text
   # card=requests.get("http://cards:5002").text
    
    if crystal== "Dolomite" or crystal =="Blue Opal" or crystal == "Astrophyllite":
        # and  card == "The Fool":
        reading = "this is your reading!!!!!!!!!!"
    else:
        reading = "this is your reverse  reading!!!!!!!!!!!"

    return reading
