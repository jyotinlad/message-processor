from scripts.messageprocessor.baseprocessor import BaseProcessor


class FeedProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("Feed")

    def process(self, data):
        self.load(data)

    def load(self, record):
        print(record)
