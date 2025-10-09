from abc import ABC, abstractmethod

from app.datastore import DataStore
from app.datastatict import DataStatistics


class ReportBase(ABC):
    """
    Базовый класс для отчётов. 
    Каждый отчёт должен реализовать методы:
    - build: формирует внутренние данные отчёта из DataStore
    - render: возвращает представление 
    """
    name: str

    def __init__(self, datastore: DataStore) -> None:
        self.datastore = datastore
        self.stats = DataStatistics()

    @abstractmethod
    def build(self) -> None:
        """Собрать внутренние данные для отчёта."""
        raise NotImplementedError

    @abstractmethod
    def render(self) -> str:
        """Вернуть строковое представление отчёта
        (для вывода в консоль)."""
        raise NotImplementedError