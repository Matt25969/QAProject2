#import pandas as pd
from  random import randint
import requests
from application import app


@app.route('/', methods=['GET','POST'])
def shufflecards():
    cards_names = [ "The Fool",
            "The Magician",
            "The High Priestess",
            "The Empress",
            "The Emperor",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgement",
            "The World" ]
    randomCard = randint(0,len(cards_names))
    #print (random_number)
    card = cards_names[randomCard]
    return card










'''
def shufflecards():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../application/cards.csv"))
    #df=pd.read_csv('../application/cards.csv')
    #give a random row
    card=df.sample(n=1) 
    #card = "The Fool"
    return card
'''
