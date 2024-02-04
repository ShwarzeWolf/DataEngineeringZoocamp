if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Remove wierd rows, create column for pickup date, rename columns to snake_case
    """
    # Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    data = data[
        (data['passenger_count'] > 0) 
        & (data['trip_distance'] > 0)
    ]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date


    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id
    data.rename(columns={
        'VendorID': 'vendor_id', 
        'RatecodeID': 'ratecode_id', 
        'PULocationID': 'pu_location_id', 
        'DOLocationID': 'do_location_id',
    }, 
    inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_no_trips_without_passengers(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

@test
def test_no_trips_with_zero_distance(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero distanse trip'

@test
def test_vendor_id_column_is_present(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' in output.columns, 'vendor_id column is not present'