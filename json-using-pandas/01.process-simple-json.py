import pandas as pd

customer_df=pd.read_json('customer.json',lines=True)

print(customer_df)