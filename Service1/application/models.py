from application import db

#reading table
class readings(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   crystal = db.Column(db.String, nullable= False)
   card= db.Card(db.String, nullable=False)

   def __repr__(self):
       return ''.join([
           'Crystal:' , self.crystal , '\r\n',
           'Card:' , self.card,
        ])
