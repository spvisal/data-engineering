import pandas as pd
import pyodbc
import sqlalchemy
import psycopg2

user_list=[
    {'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
    {'user_first_name': 'Donald', 'user_last_name': 'Duck'}
]

df=pd.DataFrame(user_list)

engine = "postgresql://retail_db_user:retail_admin@localhost:5432/retail_db"
df.to_sql('users', engine, schema='public', if_exists='append', index=False)
