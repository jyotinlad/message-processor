from .appleprocessor import AppleProcessor
from .bananaprocessor import BananaProcessor
from .kiwiprocessor import KiwiProcessor
from .orangeprocessor import OrangeProcessor
from .pearprocessor import PearProcessor


class MessageProcessor:

    def __init__(self):
        pass

    @staticmethod
    def get(processor):
        # TODO dynamically import
        # try:
        #     module_name = ".{}processor".format(processor.lower())
        #     print(module_name)
        #     # module = import_module("{}".format(module_name))
        #     module = __import__(module_name)
        #     print(module)
        #
        #     cls = getattr(module, "{}Processor".format(processor))
        #     return cls
        # except ModuleNotFoundError as e:
        #     print(e)
        #     raise NotImplementedError("{} processor not implemented".format(processor))

        if processor == "Apple":
            return AppleProcessor()
        elif processor == "Banana":
            return BananaProcessor()
        elif processor == "Kiwi":
            return KiwiProcessor()
        elif processor == "Orange":
            return OrangeProcessor()
        elif processor == "Pear":
            return PearProcessor()
        else:
            raise NotImplementedError()
