import io
import pandas as pd
import urllib.request
from io import BytesIO
import gzip

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    # List of CSV URLs
    csv_urls = [
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    ]

    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    # Initialize an empty list to store DataFrames
    data_frames = []

    # Iterate through CSV URLs
    for csv_url in csv_urls:
        print("CSV_URL= ", csv_url)

        # Download the gzip-compressed CSV file
        with urllib.request.urlopen(csv_url) as response:
            with gzip.GzipFile(fileobj=BytesIO(response.read())) as file:
                # Read the CSV file
                df = pd.read_csv(file, dtype=taxi_dtypes, parse_dates=parse_dates)

        # Append the DataFrame to the list
        data_frames.append(df)

    # Concatenate the DataFrames
    final_data = pd.concat(data_frames, ignore_index=True)

    # Display information about the loaded data
    print("Info about the loaded data:")
    print(final_data.info())

    # Further processing or analysis can be performed with 'final_data'
    # Save the concatenated DataFrame to a CSV file
    final_data.to_csv('/home/src/mage-homework/final_data.csv', index=False)
    return final_data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
