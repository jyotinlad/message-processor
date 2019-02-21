from datetime import datetime
from json import loads

import sys
sys.path.append("..")

from logger import Logger
from messageprocessor import MessageProcessor
from queue import QueueWorker


class ProcessMessages():

    def __init__(self):
        # setup queue
        self._queue = QueueWorker(name="fruits", callback=self.worker)

    @staticmethod
    def worker(ch, method, properties, body):
        data = loads(body)

        fruit = data.get("type")
        if fruit:
            # log = Logger.get()
            #
            # start_time = datetime.now()

            try:
                processor = MessageProcessor.get(fruit)
                processor.parse(data)
            except NotImplementedError as e:
                print("unknown fruit: {}".format(fruit))

            # run_time = datetime.min + (datetime.now() - start_time)
            # log.info("complete (run time: {})".format(run_time.strftime('%H:%M:%S')))

        # acknowledge message (i.e. processed)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def launch(self):
        self._queue.start()


if __name__ == "__main__":
    pm = ProcessMessages()
    pm.launch()
