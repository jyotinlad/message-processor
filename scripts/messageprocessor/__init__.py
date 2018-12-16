from .feedprocessor import FeedProcessor
from .fileprocessor import FileProcessor
from .flagprocessor import FlagProcessor


class MessageProcessor:

    def __init__(self):
        pass

    @staticmethod
    def get(processor):
        if processor == "Feed":
            return FeedProcessor()
        elif processor == "File":
            return FileProcessor()
        elif processor == "Flag":
            return FlagProcessor()
        else:
            raise NotImplementedError()
