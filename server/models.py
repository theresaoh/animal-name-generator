from sqlalchemy_db_instance import db
from sqlalchemy import Column, Integer, String

class Name(db.Model):
    __tablename__ = 'name_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    gender = db.Column(db.String(2))

class User(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35), unique=True)
    password = db.Column(db.String(35))

class Favorite(db.Model):
    __tablename__ = 'favorite_table'
    id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(35), db.ForeignKey('user_table.username'))
    name_id = db.Column(db.Integer, db.ForeignKey('name_table.id'))
    favorited_name = db.Column(db.String(40))
    name_gender = db.Column(db.String(2))

def setup_database(app):
    # create all tables with model information above
    with app.app_context():
        db.create_all()