# Тесты для app.datastore.DataStore
# Запуск
# pytest -v tests/test_datastore.py
import pytest
from contextlib import nullcontext as does_not_raise

from app.datastore import DataStore
from app.reader import Record
from app.errors import  RecordParseError


@pytest.mark.parametrize(
    "brand, expected_price, expectation", [
    ("apple",[999, 799], does_not_raise()),
    ("xiaomi",[199], does_not_raise()),
    ("samsung", [1199, 349], does_not_raise()),
])
def test_add_records_param_price(brand, 
                                expected_price, 
                                expectation,
                                populated_datastore):
    with expectation:
        ds = populated_datastore
        assert ds._brand_price[brand] == expected_price
        

@pytest.mark.parametrize(
    "brand, expected_rating, expectation", [
    ("apple", [4.9, 4.7], does_not_raise()),
    ("xiaomi", [4.6], does_not_raise()),
    ("samsung", [4.8, 4.2], does_not_raise()),
])
def test_add_records_param_rating(brand,
                           expected_rating, 
                           expectation,
                           populated_datastore):
    with expectation:
        ds = populated_datastore
        assert ds._brand_rating[brand] == expected_rating


@pytest.mark.parametrize(
    "records, expectation", [
    (
        Record(name="iphone 15 pro", 
               brand="apple", 
               price=999, 
               rating=4.9),
        does_not_raise()
    ),
    (
        Record(name="iphone 14", 
               brand="apple", 
               price=-10, 
               rating=4.0),
        pytest.raises(RecordParseError) 
    ),
    (
        Record(name="iphone 14", 
               brand="apple", 
               price=100, 
               rating=6.0),
        pytest.raises(RecordParseError) 
    ),
    (
        {"name": "iphone 14", 
         "brand": "apple", 
         "price": 799, 
         "rating": 4.7},
        pytest.raises(RecordParseError)
    )
   
])
def test_add_record(records, expectation):
    with expectation:
        ds = DataStore()
        ds.add_record(records)


@pytest.mark.parametrize("records", [
    [Record(name="iphone 15 pro", 
            brand="apple", 
            price=999, 
            rating=4.9),
     Record(name="redmi note 12", 
            brand="xiaomi", 
            price=199, 
            rating=4.6)],
    []
])
def test_add_records_multiple(records):
    ds = DataStore()
    ds.add_records(records)
    for rec in records:
        assert rec.price in ds._brand_price[rec.brand]
        assert rec.rating in ds._brand_rating[rec.brand]