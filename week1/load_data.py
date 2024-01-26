import argparse

import pandas as pd
from sqlalchemy import create_engine
import requests

from week1.config import (
    TAXI_ZONES_URL,
    TAXI_ZONES_TABLE,
    TAXI_URL,
    TAXI_TABLE,
)


def load_data(args):
    user = args.user
    password = args.password
    host = args.host
    port = args.port
    database_name = args.database_name

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database_name}')

    # loading data
    response = requests.get(TAXI_URL, params={'downloadformat': 'gz'})
    with open('taxi.csv.gz', mode='wb') as taxi_file:
        taxi_file.write(response.content)

    response = requests.get(TAXI_ZONES_URL, params={'downloadformat': 'csv'})
    with open('taxi_zones.csv', mode='wb') as taxi_zones_file:
        taxi_zones_file.write(response.content)

    # inserting data into tables
    df = pd.read_csv('taxi_zones.csv')
    df.to_sql(name=TAXI_ZONES_TABLE, con=engine, if_exists='replace')

    df_iter = pd.read_csv('taxi.csv.gz', iterator=True, chunksize=100_000)
    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.head(n=0).to_sql(name=TAXI_TABLE, con=engine, if_exists='replace')
    df.to_sql(name=TAXI_TABLE, con=engine, if_exists='append')

    for df in df_iter:
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

        df.to_sql(name=TAXI_TABLE, con=engine, if_exists='append')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='TaxiDataLoader',
        description='Loads data into postgres database',
    )

    parser.add_argument('--user', required=True)
    parser.add_argument('--password', required=True)
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', required=True, type=int)
    parser.add_argument('--database_name', required=True)

    args = parser.parse_args()

    load_data(args)

    print('All data successfully loaded')
