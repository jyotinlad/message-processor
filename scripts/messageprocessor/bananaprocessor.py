from datetime import date, timedelta

from scripts.messageprocessor.baseprocessor import BaseProcessor


class BananaProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("Banana")

    def parse(self, data):
        data["best_before"] = date.today() + timedelta(days=3)

        self.load(data)
