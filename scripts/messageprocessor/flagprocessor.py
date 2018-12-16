from scripts.messageprocessor.baseprocessor import BaseProcessor


class FlagProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("Flag")

    def process(self, data):
        self.load(data)

    def load(self, record):
        print(record)
