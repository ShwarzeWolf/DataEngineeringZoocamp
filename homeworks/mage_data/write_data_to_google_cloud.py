from pandas import DataFrame
import pyarrow as pa
import os
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/google-credentials.json'

bucket_name = 'sch-wolf-terraform-demo-terra-bucket'
project_id = 'playground-s-11-617d702b'
table_name = 'nyc_taxi_data'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table, 
        root_path=root_path, 
        partition_cols=['lpep_pickup_date'], 
        filesyse=gcs
    )
