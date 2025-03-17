import pandas as pd

#loa data
file_path = "sales_data.csv"
df = pd.read_csv(file_path)

# transform data
df['order_date'] = pd.to_datetime(df['order_date'])

df['total_price'] = df['quantity'] * df['price']

df.rename(columns={
    "order_id": "id",
    "customer_name": "customer",
    "order_date": "date"
}, inplace=True)

print(df.head())

from sqlalchemy import create_engine

# Database connection 
db_url = "postgresql://postgres:24081314@localhost:5432/sales_db"

engine = create_engine(db_url)

# Load data into PostgreSQL
df.to_sql("sales", engine, if_exists="replace", index=False)

print("Data loaded successfully!")
