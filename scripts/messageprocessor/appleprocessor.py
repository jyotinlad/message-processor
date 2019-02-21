from datetime import date, timedelta

from scripts.messageprocessor.baseprocessor import BaseProcessor


class AppleProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("Apple")

    def parse(self, data):
        data.pop("type")
        data["best_before"] = date.today() + timedelta(days=10)

        self.load(data)
