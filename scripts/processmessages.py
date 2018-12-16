from datetime import datetime

from messageprocessor import MessageProcessor


class ProcessMessages():

    def __init__(self):
        pass

    def launch(self):
        start_time = datetime.now()

        for type in ["Feed", "Flag", "File"]:
            processor = MessageProcessor.get(type)

            #TODO queue work

            print("working {} queue".format(type))

            #TODO process message
            payload = {}
            processor.process(payload)

        end_time = datetime.now() - start_time
        # print("run time {}".format(end_time.strftime("%H%M%S")))


if __name__ == "__main__":
    pm = ProcessMessages()
    pm.launch()
