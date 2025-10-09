# Тесты для app.cli
# Запуск
# pytest -v tests/test_cli.py
import pytest
from contextlib import nullcontext as does_not_raise

import app.cli as cli_module  
from app.datastore import DataStore
from app.reader import CSVReader
from app.errors import AppError
from app.reports.registry import ReportFactory


@pytest.mark.parametrize(
    "path, agregate, exeption", [
        (["a.csv", "b.csv"], "average-rating", does_not_raise()),
        (["a.csv"], "max-rating", does_not_raise()),
        (["a.csv", "b.csv", "c.csv"], "min-rating", does_not_raise()),
        (["a.csv"], "median-rating", does_not_raise()),
        (["a.csv"], "", pytest.raises(SystemExit)),
    ]
)
def test_parse_args_basic(path, agregate, exeption):
    with exeption:
        argv = ["--files", path, "--report", agregate]
        ns = cli_module.parse_args(argv)
        assert ns.files == [path]
        assert ns.report == agregate


@pytest.mark.parametrize(
    "path, agregate", [
        (["a.csv", "b.csv"], "average-rating"),
        (["a.csv"], "max-rating"),
        (["a.csv", "b.csv", "c.csv"], "min-rating"),
        (["a.csv"], "median-rating"),
    ]
)
def test_run_unexpected_exception(path, agregate, 
                                  monkeypatch, capsys):
    monkeypatch.setattr("app.cli.CSVReader", CSVReader)
    monkeypatch.setattr("app.cli.DataStore", DataStore)
    monkeypatch.setattr("app.cli.ReportFactory", ReportFactory)
    rc = cli_module.run(["--files", path, "--report", agregate])
    captured = capsys.readouterr()
    assert rc == 1
    assert "Unexpected error" in captured.err


def test_run_app_error(monkeypatch, capsys):
    class BadDataStore(DataStore):
        def add_records(self, reader):
            raise AppError("bad data", code=123)

    monkeypatch.setattr("app.cli.CSVReader", CSVReader)
    monkeypatch.setattr("app.cli.DataStore", BadDataStore)
    monkeypatch.setattr("app.cli.ReportFactory", ReportFactory)
    rc = cli_module.run(["--files", "f.csv",
                         "--report", "average-rating"])
    captured = capsys.readouterr()
    assert rc == 2
    assert "Error 123" in captured.err