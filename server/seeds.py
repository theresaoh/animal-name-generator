import pandas as pd
from sqlalchemy_db_instance import db
from app import create_app

app = create_app()
with app.app_context():
	engine = db.get_engine()
	csv_file_path = 'Names.csv'

	# Read CSV (Names.csv) with Pandas
	with open(csv_file_path, 'r') as file:
		df = pd.read_csv(file)

		# Insert to DB
		df.to_sql('name_table',
			con=engine,
			index_label='id',
			if_exists='append',
			chunksize=100
		)
        
        