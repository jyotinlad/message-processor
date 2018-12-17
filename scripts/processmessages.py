from datetime import datetime

from logger import Logger
from messageprocessor import MessageProcessor


class ProcessMessages():

    def __init__(self):
        self.log = Logger.get()

    def launch(self):
        start_time = datetime.now()

        for type in ["Feed", "Flag", "File"]:
            processor = MessageProcessor.get(type)

            #TODO queue work

            self.log.info("working {} queue".format(type))

            #TODO process message
            payload = {}
            processor.process(payload)

        run_time = datetime.min + (datetime.now() - start_time)
        self.log.info("complete (run time: {})".format(run_time.strftime('%H:%M:%S')))


if __name__ == "__main__":
    pm = ProcessMessages()
    pm.launch()
