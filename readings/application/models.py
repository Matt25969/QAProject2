from application import db

#reading table
class readings(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   crystal = db.Column(db.String(100), nullable= False)
   card= db.Column(db.String(100), nullable=False)
   reading= db.Column(db.String(1000), nullable=False)

   def __repr__(self):
       return ''.join([
           'Crystal:' , self.crystal ,
           'Card:' , self.card ,
           'Meaning:', self.reading, '\r\n',
        ])
