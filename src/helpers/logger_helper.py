import inspect
import logging


def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    file_handler = logging.FileHandler('log_files/logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # filehandler object

    logger.setLevel(logging.DEBUG)  # debug and up will print
    return logger
