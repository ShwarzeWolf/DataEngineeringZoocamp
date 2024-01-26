import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# loading taxi zones data
df = pd.read_csv('sources/taxi+_zone_lookup.csv')
df.to_sql(name='green_taxi_zones_data', con=engine, if_exists='replace')

# loading taxi  data
df_iter = pd.read_csv('sources/green_tripdata_2019-09.csv', iterator=True, chunksize=100000)
df = next(df_iter)

df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')
df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

for df in df_iter:
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.to_sql(name='green_taxi_data', con=engine, if_exists='append')