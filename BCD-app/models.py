# import db object from flask app
from app import db

# database tables


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(100), nullable=False)
