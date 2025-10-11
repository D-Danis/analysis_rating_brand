from typing import Dict, Type

from ..datastore import DataStore
from .base import ReportBase
from .price import (AveragePrice,
                    MaxPrice,
                    MedianPrice,
                    MinPrice)
from .rating import (AverageRating,
                     MaxRating,
                     MedianRating,
                     MinRating)
from ..errors import ReportError


class ReportFactory:
    """
    Фабрика отчётов.
    """
    _registry: Dict[str, Type[ReportBase]] = {
        AveragePrice.name: AveragePrice,
        MaxPrice.name: MaxPrice,
        MinPrice.name: MinPrice,
        MedianPrice.name: MedianPrice,
        AverageRating.name: AverageRating,
        MaxRating.name: MaxRating,
        MinRating.name: MinRating,
        MedianRating.name: MedianRating
    }

    @classmethod
    def create(cls, 
               name: str, 
               datastore: DataStore, 
               **kwargs: object) -> ReportBase:
        ctor = cls._registry.get(name)
        if not ctor:
            raise ReportError(
                f"Unknown report: {name}", 
                code="report.unknown")
        return ctor(datastore, **kwargs)