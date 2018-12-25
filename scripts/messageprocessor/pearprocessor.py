from datetime import date, timedelta

from scripts.messageprocessor.baseprocessor import BaseProcessor


class PearProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("Pear")

    def parse(self, data):
        data["best_before"] = date.today() + timedelta(days=10)

        self.load(data)
