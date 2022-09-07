import pandas as pd
import psycopg2
query = 'SELECT * FROM users'
conn = 'postgresql://retail_db_user:retail_admin@localhost:5432/retail_db'
df = pd.read_sql(query,conn)

print(df)
