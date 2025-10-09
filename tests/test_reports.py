# Тесты для app.reports
# Запуск
# pytest -v tests/test_reports.py
import pytest
from contextlib import nullcontext as does_not_raise
from tabulate import tabulate

from app.datastore import DataStore
from app.errors import ReportError
from app.reports.base import ReportBase
from app.reports.registry import ReportFactory
from app.reports.rating.average_rating import AverageRating
from app.reports.rating.max_rating import MaxRating
from app.reports.rating.median_rating import MedianRating
from app.reports.rating.min_rating import MinRating
from tests.conftest import normalize_table_str


@pytest.mark.parametrize(
    " reports, expected, extra, expectation ",
    [
        (AverageRating,
        [('apple', 4.800000000000001),
         ('xiaomi', 4.6), 
         ('samsung', 4.5)],
        {"precision":2}, 
        does_not_raise()),
        (
            MaxRating, 
            [('apple', 4.9), 
             ('samsung', 4.8), 
             ('xiaomi', 4.6)],
            {"precision":2}, 
            does_not_raise()
         ),
        (
            MinRating, 
            [('apple', 4.7), 
             ('xiaomi', 4.6), 
             ('samsung', 4.2)],
            {"precision":2}, 
            does_not_raise()
         ),
        (
            MedianRating, 
            [('apple', 4.800000000000001), 
             ('xiaomi', 4.6)],
            {"precision":2, "top":2}, 
            does_not_raise()
         )
        
    ]
)
def test_agregate_rating_reports(reports, 
                                 expected, 
                                 extra, 
                                 expectation, 
                                 populated_datastore):
    with expectation:
        ds = populated_datastore
        rpt = reports(ds, **extra )
        rpt.build()
        assert rpt._rows == expected


@pytest.mark.parametrize(
    " reports, table, extra, expectation ",
    [
        (AverageRating,
        [("apple", f"{4.8:.1f}"),
         ("xiaomi", f"{4.6:.1f}")],
        {"precision":1, "top":2}, 
        does_not_raise()),
        (
            MaxRating, 
            [('apple', 4.9), 
             ('samsung', 4.8), 
             ('xiaomi', 4.6)],
            {"precision":2}, 
            does_not_raise()
         ),
        (
            MinRating, 
            [('apple', 4.7), 
             ('xiaomi', 4.6), 
             ('samsung', 4.2)],
            {"precision":2}, 
            does_not_raise()
         ),
        (
            MedianRating, 
            [('apple', 4.8), ('xiaomi', 4.6)], 
            {"precision":1, "top":2}, 
            does_not_raise()
         )
        
    ]
)
def test_agregate_render_precision(reports, 
                                   table, 
                                   extra, 
                                   expectation,
                                   populated_datastore):
    with expectation:
        ds = populated_datastore
        rpt = reports(ds, **extra )
        rpt.build()
        rendered = rpt.render()
        headers = ("brand", "rating")
        expected = tabulate(table, 
                            headers=headers, 
                            tablefmt="github", 
                            stralign="left", 
                            numalign="right")
        assert normalize_table_str(rendered)\
            == normalize_table_str(expected)


@pytest.mark.parametrize(
    "extra",
    [
        {"one": 1, "2":"2"}, 
        {"2":"2"},
        {"precision":2 , "top":5},
        {"precision":2 , "top":5,"one": 1, "2":"2"},
        {"":""},
        {}
    ]
)
def test_report_factory_kwargs_passed(monkeypatch,
                                      extra):
    called = {}
    def fake_ctor(ds, **kwargs):
        called['datastore'] = ds
        called['kwargs'] = kwargs
        class Dummy(ReportBase):
            name = "dummy"
            def __init__(self, ds, **kwargs):
                super().__init__(ds)
            def build(self):pass
            def render(self):pass
        return Dummy(ds)

    ReportFactory._registry['dummy'] = fake_ctor  
    registry_name = "_registry"
    try:
        datastore = DataStore()
        ReportFactory.create('dummy', datastore, **extra)
        assert called['datastore'] is datastore
        assert called['kwargs'] == {**extra}
    finally:
        getattr(ReportFactory, registry_name).pop('dummy', None)  

       
@pytest.mark.parametrize(
    "name, expectation", 
    [
        (
            "non-existent-report", 
            pytest.raises(ReportError)
        ),
        (
            AverageRating.name, 
            does_not_raise()
        ),
        (
            MaxRating.name, 
            does_not_raise()
        ),
        (
            MinRating.name, 
            does_not_raise()
        ),
        (
            MedianRating.name, 
            does_not_raise()
        )
    ]
)
def test_report_factory_positive_negative(name, 
                                          expectation):
    with expectation:
        ds = DataStore()
        r = ReportFactory.create(name, ds)
        assert isinstance(r, ReportBase)

        
@pytest.mark.parametrize(
    "performance, expectation",
    [
        (
            AverageRating, 
            does_not_raise()
        ),
        (
            MaxRating, 
            does_not_raise()
        ),
        (
            MinRating, 
            does_not_raise()
        ),
        (
            MedianRating, 
            does_not_raise()
        ),
        (
            "non-existent-report", 
            pytest.raises(AttributeError)
        )
    ]
)      
def test_report_factory_registered_reports(performance,
                                           expectation):
    with expectation:
        ds = DataStore()
        regist = ReportFactory.create(performance.name, ds)
        assert isinstance(regist, ReportBase)
        assert isinstance(regist, performance)


@pytest.mark.parametrize(
    "registered_ctor, expect_instance, expect_isinstance",
    [
        (
            lambda ds, **kwargs: 
                _make_dummy_instance(implement_build=True),
            True,
            True,
        ),
        (
            lambda datastore, **kwargs: object(),
            True,
            False,
        ),
    ],
)
def test_create_and_isinstance(registered_ctor, 
                               expect_instance, 
                               expect_isinstance):
    ds = DataStore()
    ReportFactory._registry['dummy'] = registered_ctor 
    r = ReportFactory.create('dummy', ds, opt1=1, opt2="x")
    assert (r is not None) == expect_instance
    assert isinstance(r, ReportBase) is expect_isinstance


def _make_dummy_instance(implement_build: bool):
    ds = DataStore()
    class Dummy(ReportBase):
        name = "dummy"
        if implement_build:
            def build(self):
                return None
        else:
            pass
        def render(self):
            return "rendered"
    if not implement_build:
        return object()
    return Dummy(ds)