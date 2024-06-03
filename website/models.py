from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    
class Movie(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    movie_name=db.Column(db.String(150))
    poster_url=db.Column(db.String(1000))
    year=db.Column(db.String(10))
    imdb=db.Column(db.String(150))
    type_movie=db.Column(db.String(150))

class Playlist(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     userid=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     movie=db.Column(db.Integer, db.ForeignKey('movie.id'),nullable=False)

