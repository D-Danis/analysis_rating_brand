from typing import Dict, Type

from .base import ReportBase


_registry: Dict[str, Type['ReportBase']] = {}


def register_command(cls):
    """декоратор для регистрации команды по имени."""
    _registry[cls.name] = cls
    return cls