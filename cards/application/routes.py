import pandas as pd
import random

def shufflecards():
    df=pd.read_csv('/cards/application/cards.csv')
    #give a random row
    card=df.sample(n=1) 
    return card
