from ..datastore import DataStore
from ..errors import ReportError
from .base import ReportBase
from .registry import _registry


class ReportFactory:
    """
    Фабрика отчётов.
    """
    _registry = _registry
    @classmethod
    def create(cls, name: str, datastore: DataStore, **kwargs: object) -> ReportBase:
        ctor = cls._registry.get(name)
        if not ctor:
            raise ReportError(f"Unknown report: {name}", code="report.unknown")
        return ctor(datastore, **kwargs)