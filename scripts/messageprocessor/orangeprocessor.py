from datetime import date, timedelta

from scripts.messageprocessor.baseprocessor import BaseProcessor


class OrangeProcessor(BaseProcessor):

    def __init__(self):
        super().__init__("Orange")

    def parse(self, data):
        data["best_before"] = date.today() + timedelta(days=7)

        self.load(data)
