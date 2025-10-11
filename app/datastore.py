from collections import defaultdict
from typing import Dict, List, Iterable

from .reader import Record
from .errors import RecordParseError


class DataStore:
    """Хранилище агрегированных данных."""
    def __init__(self) -> None:
        self._brand_rating: Dict[str, List[float]] = defaultdict(list)
        self._brand_price: Dict[str, List[float]] = defaultdict(list)

    def add_record(self, record: Record) -> None:
        if not isinstance(record, Record):
            raise RecordParseError("Expected Record object")
        
        if not record.brand:
            raise RecordParseError("The 'brand' field cannot be empty or None.")

        if not isinstance(record.price, (int, float)) or record.price < 0:
            raise RecordParseError("The 'price' must be a non-negative number")

        if not isinstance(record.rating, (int, float)) or not (0 <= record.rating <= 5):
            raise RecordParseError("The 'rating' must be between 0 and 5.")

        self._brand_rating[record.brand].append(record.rating)
        self._brand_price[record.brand].append(record.price)

    def add_records(self, records: Iterable[Record]) -> None:
        if not isinstance(records, Iterable):
            raise RecordParseError("Expected Iterable object")
        
        for record in records:
            self.add_record(record)
