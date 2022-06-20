import logging
import os
import datetime

class MyLogger:
    _logger = None
    _level = logging.INFO
    _formater = False
    def __new__(cls, *args, **kwargs):
        if cls._logger is None:
            cls._logger = super().__new__(cls, *args, **kwargs)
            cls._logger = logging.getLogger("Desafio_Eng_ML \n")
            cls._logger.setLevel(cls._level)
            formatter = logging.Formatter(
                '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

            now = datetime.datetime.now()
            dirname = "./log"

            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fileHandler = logging.FileHandler(
                dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")

            streamHandler = logging.StreamHandler()
            if cls._formater:
                fileHandler.setFormatter(formatter)
                streamHandler.setFormatter(formatter)

            cls._logger.addHandler(fileHandler)
            cls._logger.addHandler(streamHandler)

        return cls._logger


# a simple usecase
if __name__ == "__main__":
    logger = MyLogger()
    logger.info("Hello, Logger")
    logger = MyLogger()
    logger.debug("bug occured")