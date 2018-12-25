from argparse import ArgumentParser
from json import dumps
from random import randint

from queue import Queue


_FRUITS = ["Apple", "Banana", "Kiwi", "Orange", "Pear"]
_CONDITION = ["Good", "Bad"]

_APPLE_COLOURS = ["Green", "Pink", "Red"]
_PEAR_COLOURS = ["Brown", "Green", "Yellow"]


def send(**kwargs):
    quantity = kwargs.get("quantity")
    debug = kwargs.get("debug")
    queue = Queue(name="fruits")

    for counter in range(1, quantity):
        # define fruit
        fruit = _FRUITS[randint(0, len(_FRUITS) - 1)]
        message = {
            "type": fruit,
            "weight": randint(30, 50),
            "condition": _CONDITION[randint(0, len(_CONDITION) - 1)]
        }

        # set colour
        if fruit == "Apple":
            message["colour"] = _APPLE_COLOURS[randint(0, len(_APPLE_COLOURS) - 1)]
        elif fruit == "Banana":
            message["colour"] = "Yellow"
        elif fruit == "Kiwi":
            message["colour"] = "Brown"
        elif fruit == "Orange":
            message["colour"] = "Orange"
        elif fruit == "Pear":
            message["colour"] = _PEAR_COLOURS[randint(0, len(_PEAR_COLOURS) - 1)]

        print("sending {type} message".format(**message))
        queue.send(dumps(message))


if __name__ == "__main__":
    # define script arguments..
    parser = ArgumentParser(description="send fruit messages")
    parser.add_argument("-q", dest="quantity", type=int, required=False, help="Quantity.", default=10)
    parser.add_argument("--debug", action="store_true", help="debug")

    # parse script arguments
    args = parser.parse_args()

    send(**vars(args))
