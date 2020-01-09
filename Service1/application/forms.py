from flask_wtf import FlaskForm
from wtforms import SubmitField

#button to select a crystal
class CrystalGenerator(FlaskForm):
    submit = SubmitField("Find your crystal")

#button to select a card
class CardGenerator(FlaskForm):
    submit=SubmitField("Shuffle deck")

