import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection string
conn_string = 'mysql+pymysql://root:Paras%40123@127.0.0.1/SQL_Buisness'
db = create_engine(conn_string)
conn = db.connect()

# List of CSV files
files = ['Fact', 'Location', 'Product']

# Correcting file path usage
base_path = r"E:\Personal Resources_DA\SQL\Project\Buisness Dataset\Dataset"

for file in files:
    try:
        file_path = os.path.join(base_path, f"{file}.csv")  # Properly join paths
        df = pd.read_csv(file_path, encoding="utf-8")  # Handle encoding issues
        df.to_sql(file, con=conn, if_exists='replace', index=False)
        print(f"Successfully inserted {file}.csv into database")
    except Exception as e:
        print(f"Error inserting {file}.csv: {e}")

# Close connection
conn.close()
