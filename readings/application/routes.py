from flask import render_template, redirect, url_for
from application import app
import requests

@app.route("/", methods= ["GET", "POST"])
def reading():
    crystal_service = "http://crystal:5000/"
    card_service = "http://card:5000/"
    if crystal_service == "Dolomite" or crystal_service =="Blue Opal" or crystal_service == "Astrophyllite" and  card_service == "The Fool":
        reading = "this is your reading"
    else:
        reading = "this is your reverse  reading"
    
    return reading
