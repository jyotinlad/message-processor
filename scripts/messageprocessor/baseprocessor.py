from abc import ABC, abstractmethod


class BaseProcessor(ABC):

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def process(self, data):
        raise NotImplementedError()

    @abstractmethod
    def load(self, record):
        raise NotImplementedError()
