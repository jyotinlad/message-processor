from pika import BasicProperties, BlockingConnection, ConnectionParameters


class Queue:

    def __init__(self, name):
        # set queue name
        self.name = name

        # setup queue connection and channel
        self._conn = BlockingConnection(ConnectionParameters(host='localhost'))
        self._channel = self._conn.channel()
        self._channel.queue_declare(queue=self.name, durable=True)

    def send(self, message):
        self._channel.basic_publish(exchange='',
                                    routing_key=self.name,
                                    body=message,
                                    properties=BasicProperties(
                                        delivery_mode=2,  # make message persistent
                                        )
                                    )

    def __del__(self):
        self._conn.close()


class QueueWorker(Queue):

    def __init__(self, name, callback):
        # check and set callback function
        if hasattr(callback, "__call__"):
            #TODO check supplied args if possible
            self._callback = callback
        else:
            raise TypeError("function must be a callable function")

        super().__init__(name)

    def start(self):
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(self._callback, queue=self.name)

        print("waiting for messages (press CTRL+C to exit)..")
        self._channel.start_consuming()
