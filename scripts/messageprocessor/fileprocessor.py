from scripts.messageprocessor.baseprocessor import BaseProcessor


class FileProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("File")

    def process(self, data):
        self.load(data)

    def load(self, record):
        print(record)
