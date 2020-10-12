import logging

class LogGen:
    @staticmethod
    def getlogger():
        logging.basicConfig(filename=".\\Logs\\"+"automation.log",filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s: ',
                            datefmt='%m/%d/%y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


