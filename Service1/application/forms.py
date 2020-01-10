from flask_wtf import FlaskForm
from wtforms import SubmitField

#button to get reading
class ReadingGenerator(FlaskForm):
    
    submit = SubmitField("Shuffle!")


