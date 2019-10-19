from sqlalchemy_db_instance import db

class Name(db.Model):
    __tablename__ = 'name_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    gender = db.Column(db.String(2))
