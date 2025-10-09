import statistics
from typing import Dict, List


class DataStatistics:
    """Обработка данных: вычисления статистик"""
    
    @staticmethod
    def average(data: Dict[str, List[float]]) -> Dict[str, float]:
        return {k: sum(v)/len(v) for k, v in data.items() if v}
    
    @staticmethod
    def maximum(data: Dict[str, List[float]]) -> Dict[str, float]:
        return {k: max(v) for k, v in data.items() if v}
    
    @staticmethod
    def minimum(data: Dict[str, List[float]]) -> Dict[str, float]:
        return {k: min(v) for k, v in data.items() if v}
    
    @staticmethod
    def median(data: Dict[str, List[float]]) -> Dict[str, float]:
        return {k: statistics.median(v) for k, v in data.items() if v}