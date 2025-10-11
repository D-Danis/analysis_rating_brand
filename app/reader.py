import csv
from dataclasses import dataclass
from typing import Iterable, Iterator, List

from .errors import FileReadError, CSVFormatError,\
                        RecordParseError


@dataclass
class Record:
    name: str
    brand: str
    price: int
    rating: float


class CSVReader:
    REQUIRED_FIELDS = {"name", 
                       "brand", 
                       "price", 
                       "rating"}

    def __init__(self, 
                 paths: Iterable[str], 
                 encoding: str = "utf-8") -> None:
        self.paths: List[str] = list(paths)
        self.encoding = encoding

    def __iter__(self) -> Iterator[Record]:
        for path in self.paths:
            try:
                with open(path, 
                          newline="", 
                          encoding=self.encoding) as fh:
                    reader = csv.DictReader(fh)
                    if not reader.fieldnames:
                        raise CSVFormatError(
                            f"Empty or missing header in {path}", 
                            code="csv.header.missing")
                    fields = {fn.strip() for fn in reader.fieldnames if fn}
                    if not self.REQUIRED_FIELDS.issubset(fields):
                        raise CSVFormatError(
                            f"Required columns missing in {path}", 
                            code="csv.columns.missing")
                    for line_no, row in enumerate(reader, start=2):
                        try:
                            name = (row.get("name") or "").strip()
                            if not name:
                                continue
                            price_raw = (row.get("price") or "").strip()
                            price = int(price_raw)
                            rating_raw = (row.get("rating") or "").strip()
                            rating = float(rating_raw)
                            yield Record(
                                name=name,
                                brand=(row.get("brand") or "").strip(),
                                price=price,
                                rating=rating,
                            )
                        except ValueError:
                            raise RecordParseError(
                                f"Invalid price at {path}:{line_no}", 
                                code="record.price.invalid")
            except FileNotFoundError as exc:
                raise FileReadError(f"File not found: {path}") from exc
            except OSError as exc:
                raise FileReadError(f"Error reading file: {path}") from exc
            