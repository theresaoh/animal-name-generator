import pandas as pd

def seed():
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
            chunksize=10)