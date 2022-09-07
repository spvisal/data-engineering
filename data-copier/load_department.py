import pandas as pd
import os

conn = 'postgresql://retail_db_user:retail_admin@localhost:5432/retail_db'

BASE_DIR="C:\\Users\\SAURABH\\Desktop\\Python\\data-engineering\\data-copier\\Research\\data\\retail_db_json\\"

table_name='departments'

file_name=os.listdir(f'{BASE_DIR}{table_name}')[0]
fp=f'{BASE_DIR}{table_name}\{file_name}'

#Read data
df=pd.read_json(fp,lines=True)
df.to_sql(table_name, conn, if_exists='append', index=False)