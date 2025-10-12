import csv
from pathlib import Path
from typing import List

import pytest

from app import DataStore, Record


def write_csv(path: Path, header: List[str], rows: List[List | str]):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


@pytest.fixture
def write_csv_fn(tmp_path):
    def _write(name: str, header: list[str], rows: list[list]):
        p = tmp_path / name
        write_csv(p, header, rows)
        return str(p)

    return _write


def normalize_table_str(s: str) -> str:
    return "\n".join(line.rstrip() for line in s.strip().splitlines())


@pytest.fixture
def sample_records():
    def makerecord(name: str, brand: str, price: int, rating: float):
        return Record(name=name, brand=brand, price=price, rating=rating)

    return makerecord


@pytest.fixture
def populated_datastore(sample_records):
    ds = DataStore()
    records = (
        sample_records("iphone 15 pro", "apple", 999, 4.9),
        sample_records("galaxy s23 ultra", "samsung", 1199, 4.8),
        sample_records("redmi note 12", "xiaomi", 199, 4.6),
        sample_records("iphone 14", "apple", 799, 4.7),
        sample_records("galaxy a54", "samsung", 349, 4.2),
    )
    ds.add_records(records)
    return ds
