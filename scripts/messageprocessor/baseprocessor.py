from abc import ABC, abstractmethod
from database import Database
from datetime import date
from os import path


_STORAGE_DIR = path.join("..", "storage")


class BaseProcessor(ABC):

    def __init__(self, type):
        self.type = type

        self._table = "{}s".format(type.lower())
        self._db = Database()

    @abstractmethod
    def parse(self, data):
        raise NotImplementedError()

    @staticmethod
    def converter(o):
        if isinstance(o, date):
            return o.__str__()

    def load(self, record):
        self._db.insert(self._table, record)
