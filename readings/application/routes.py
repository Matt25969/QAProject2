from flask import render_template, redirect, url_for
from application import app
import requests

@app.route("/", methods= ["GET", "POST"])
def reading():
    crystal_service = requests.get("http://crystal:5001/").text
    card_service=requests.get("http://card:5002/").text
    if crystal_service == "Dolomite" or crystal_service =="Blue Opal" or crystal_service == "Astrophyllite" and  card_service == "The Fool":
        reading = "this is your reading"
    else:
        reading = "this is your reverse  reading"

    return reading
