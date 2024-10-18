from .settings import db
from flask_login import UserMixin

class Tours(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    date = db.Column(db.String())
    country = db.Column(db.String())
    price = db.Column(db.String())
    description = db.Column(db.Text())

    def __repr__(self) -> str:
        return f"назва подорожі - {self.title}" 
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __repr__(self) -> str:
        return f"користувач - {self.username}"
    

