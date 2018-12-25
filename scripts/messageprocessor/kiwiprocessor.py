from datetime import date, timedelta

from scripts.messageprocessor.baseprocessor import BaseProcessor


class KiwiProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("Kiwi")

    def parse(self, data):
        data["best_before"] = date.today() + timedelta(days=5)

        self.load(data)
