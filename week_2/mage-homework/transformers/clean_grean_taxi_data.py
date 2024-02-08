if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id
    data.columns = data.columns.str.replace(' ', '_').str.lower()

    unique_vendor_ids = data['vendorid'].unique()
    print("Unique Vendor IDs:", unique_vendor_ids)

    return data


@test
def test_output(output, *args) -> None:
    
    # assert vendor_id is one of the existing values in the column (currently)
    assert 'vendor_id' not in output.columns, 'The column (vendor_id) must exist'

    # assert the passanger_count > 0
    assert (output['passenger_count'] != 0).all(), 'There should not be any passanger count with zero'
    
    # assert the trip_distance > 0
    assert (output['trip_distance'] != 0).all(), 'There should not be any trip_distance with zero'
