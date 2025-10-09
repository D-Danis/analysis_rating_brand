from typing import Dict, Type

from app.datastore import DataStore
from app.reports.base import ReportBase
from app.reports.price.average_price import AveragePrice
from app.reports.price.max_price import MaxPrice
from app.reports.price.median_rating import MedianPrice
from app.reports.price.min_price import MinPrice
from app.reports.rating.average_rating import AverageRating
from app.reports.rating.max_rating import MaxRating
from app.reports.rating.min_rating import MinRating
from app.reports.rating.median_rating import MedianRating
from app.errors import ReportError


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