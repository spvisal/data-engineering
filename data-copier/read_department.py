import pandas as pd
import os

conn = 'postgresql://retail_db_user:retail_admin@localhost:5432/retail_db'

query="SELECT * FROM departments"

df=pd.read_sql(query,conn)
print(df)