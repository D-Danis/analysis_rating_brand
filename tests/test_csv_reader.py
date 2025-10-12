# Тесты для app.reader.CSVReader
# Запуск
# pytest -q tests/test_csv_reader.py
import pytest
from contextlib import nullcontext as does_not_raise

from app import CSVReader, Record, CSVFormatError, RecordParseError, FileReadError


@pytest.mark.parametrize(
    "headers, expectation",
    [
        (["iphone 15 pro", "apple", 999, 4.9], does_not_raise()),
        (["iphone 15 pro", "apple", 999, ""], pytest.raises(RecordParseError)),
        (["iphone 15 pro", "apple", "", 4.9], pytest.raises(RecordParseError)),
        (["iphone 15 pro", "", 999, 4.9], does_not_raise()),
        (["apple", 999, 4.9], pytest.raises(RecordParseError)),
    ],
)
def test_read_single_files(headers, expectation, write_csv_fn):
    header = ["name", "brand", "price", "rating"]
    with expectation:
        p = write_csv_fn("one.csv", header, [headers])
        reader = CSVReader([p])
        records = list(reader)
        r = records[0]
        assert isinstance(r, Record)
        assert r.name == headers[0]
        assert r.brand == headers[1]
        assert r.price == headers[2]
        assert r.rating == headers[3]


@pytest.mark.parametrize(
    "headers, count",
    [
        ([["iphone 15 pro", "apple", 999, 4.9]], 1),
        (
            [
                ["iphone 15 pro", "apple", 999, 4.9],
                ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ],
            2,
        ),
        (
            [
                ["iphone 15 pro", "apple", 999, 4.9],
                ["galaxy s23 ultra", "samsung", 1199, 4.8],
                ["redmi note 12", "xiaomi", 199, 4.6],
            ],
            3,
        ),
    ],
)
def test_read_single_len_option(headers, count, write_csv_fn):
    header = ["name", "brand", "price", "rating"]
    p = write_csv_fn("one.csv", header, headers)
    reader = CSVReader([str(p)])
    records = list(reader)
    assert len(records) == count


@pytest.mark.parametrize(
    "header1, header2, expected_brand",
    [
        (
            [["iphone 15 pro", "apple", 999, 4.9]],
            [
                ["galaxy s23 ultra", "samsung", 1199, 4.8],
                ["redmi note 12", "xiaomi", 199, 4.6],
            ],
            ["apple", "samsung", "xiaomi"],
        ),
        (
            [["galaxy s23 ultra", "samsung", 1199, 4.8]],
            [["redmi note 12", "xiaomi", 199, 4.6]],
            ["samsung", "xiaomi"],
        ),
        (
            [
                ["iphone 15 pro", "apple", 999, 4.9],
                ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ],
            [["redmi note 12", "xiaomi", 199, 4.6]],
            ["apple", "samsung", "xiaomi"],
        ),
    ],
)
def test_read_multiple_files_and_rows(header1, header2, expected_brand, write_csv_fn):
    header = ["name", "brand", "price", "rating"]
    p1 = write_csv_fn("a.csv", header, header1)
    p2 = write_csv_fn("b.csv", header, header2)
    reader = CSVReader([str(p1), str(p2)])
    records = list(reader)
    assert [r.brand for r in records] == expected_brand


@pytest.mark.parametrize(
    "error, expectatio",
    [
        ("nonexistentfile12345.csv", pytest.raises(FileReadError)),
        (["nonexistentfile12345.csv"], pytest.raises(FileReadError)),
    ],
)
def test_file_notfound_raises_FileReadError(error, expectatio):
    with expectatio:
        reader = CSVReader(error)
        list(reader)


def test_missing_header_raises_CSVFormatError(tmp_path):
    p = tmp_path / "noheader.csv"
    p.write_text("", encoding="utf-8")
    reader = CSVReader([str(p)])
    with pytest.raises(CSVFormatError):
        list(reader)
