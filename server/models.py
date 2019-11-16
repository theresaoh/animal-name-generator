from sqlalchemy_db_instance import db

class Name(db.Model):
    __tablename__ = 'name_table'
    id = db.Column(db.Integer, primary_key=True)
    AnimalName = db.Column(db.String(500))
    Sex = db.Column(db.String(2))

class User(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35))
    password = db.Column(db.String(35))

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(35), db.ForeignKey('user_table.id'))
    name_id = db.Column(db.String(35), db.ForeignKey('name_table.id'))

def setup_database(app):
    with app.app_context():
        engine = db.get_engine()
        Base.metadata.create_all(engine)

        csv_file_path = 'Names.csv'

        # Read CSV with Pandas
        with open(csv_file_path, 'r') as file:
            df = pd.read_csv(file)

        # Insert to DB
        df.to_sql('name_table',
                con=engine,
                index_label='id',
                if_exists='replace')