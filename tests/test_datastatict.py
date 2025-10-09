# Тесты для app.datastatict.DataStatict
# Запуск
# pytest -v tests/test_datastatict.py
import pytest
from contextlib import nullcontext as does_not_raise

from app.datastatict import DataStatistics


@pytest.mark.parametrize(
    "metod, expected_price, expectation",
    [
        (
            DataStatistics().average, 
            {'apple': 899.0, 
             'samsung': 774.0, 
             'xiaomi': 199.0},
            does_not_raise()
         ),
        (
            DataStatistics().maximum, 
            {'apple': 999, 
             'samsung': 1199, 
             'xiaomi': 199},
            does_not_raise()
         ),
        (
            DataStatistics().minimum, 
            {'apple': 799, 
             'samsung': 349, 
             'xiaomi': 199},
            does_not_raise()
         ),
        (
            DataStatistics().median, 
            {'apple': 899.0, 
             'samsung': 774.0, 
             'xiaomi': 199},
            does_not_raise()
         )
    ]
)
def test_agregate_price(metod, 
                        expected_price, 
                        expectation,
                        populated_datastore):
    with expectation:
        assert expected_price == metod(
            populated_datastore._brand_price)
        

@pytest.mark.parametrize(
    "metod, expected_rating, expectation",
    [
        (
            DataStatistics().average, 
            {'apple': 4.800000000000001, 
             'xiaomi': 4.6, 
             'samsung': 4.5},
            does_not_raise()
         ),
        (
            DataStatistics().maximum, 
            {'apple': 4.9, 
             'samsung': 4.8, 
             'xiaomi': 4.6},
            does_not_raise()
         ),
        (
            DataStatistics().minimum, 
            {'apple': 4.7, 
             'xiaomi': 4.6, 
             'samsung': 4.2},
            does_not_raise()
         ),
        (
            DataStatistics().median, 
            {'apple': 4.800000000000001, 
             'xiaomi': 4.6, 
             'samsung': 4.5},
            does_not_raise()
         )
    ]
)
def test_agregate_rating(metod, 
                         expected_rating, 
                         expectation,
                         populated_datastore):
    with expectation:
        assert expected_rating == metod(
            populated_datastore._brand_rating)