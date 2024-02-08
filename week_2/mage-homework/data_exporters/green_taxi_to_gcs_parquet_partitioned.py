import pyarrow as pa
import pyarrow.parquet as pq
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/dtc-de-course-412309-f4bc0b7a3b64.json'
bucket_name = 'mage-zoomcamp-asaad'
project_id = 'dtc-de-course-412309'
table_name = 'green_taxi_data'
root_path = f'{bucket_name}/${table_name}'


@data_exporter
def export_data(data, *args, **kwargs):
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date 
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )

