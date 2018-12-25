from abc import ABC, abstractmethod
from datetime import date
from json import dumps, load
from os import path


_STORAGE_DIR = path.join("..", "storage")


class BaseProcessor(ABC):

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def parse(self, data):
        raise NotImplementedError()

    @staticmethod
    def converter(o):
        if isinstance(o, date):
            return o.__str__()

    def load(self, record):
        data = []

        filename = "{}.tsv".format(self.type)
        file = path.join(_STORAGE_DIR, filename)
        if path.isfile(file):
            with open(file, "r") as fh:
                data = load(fh)

        data.append(record)

        with open(file, "w+") as fh:
            fh.write(dumps(data, default=self.converter, indent=4))
