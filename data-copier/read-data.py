# Before working on data project one must understand the data.
# 1. Get non NULL count of each attributes
# 2. Get the names and data types of each attributes.
# 3. Project some of the fields in the DataFrame.
# 4. Filter the data for a given order_item_order_id

import json
import os
import pandas as pd

file_location='C:\\Users\\SAURABH\\Desktop\\Python\\data-engineering\\data-copier\\Research\\data\\retail_db_json\\order_items\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'

read_data_df=pd.read_json(file_location,lines=True)

#print(read_data_df.count())

#print(read_data_df.describe())

#print(read_data_df.columns)

#print(read_data_df.dtypes)

#print(read_data_df[['order_item_order_id','order_item_subtotal']])

#print(read_data_df[read_data_df['order_item_order_id']==2])

# Reading the data in chunks and then create the DataFrame

# json_reader=pd.read_json(file_location,lines=True,chunksize=1000)

# for idx,df in enumerate(json_reader):
#     print(f'Number of records in chunk with index {idx} is {df.shape[0]}')

# Reading the data dynamically

BASE_DIR="C:\\Users\\SAURABH\\Desktop\\Python\\data-engineering\\data-copier\\Research\\data\\retail_db_json\\"

table_name="order_items\\"

file_name=os.listdir(f'{BASE_DIR}{table_name}')[0]
fp=f'{BASE_DIR}{table_name}{file_name}'

df=pd.read_json(fp,lines=True)

print(df)