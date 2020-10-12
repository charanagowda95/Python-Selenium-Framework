import logging

logging.basicConfig(filename='.\\Logs\\automation.log',filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s: ',
                            datefmt='%m/%d/%y %I:%M:%S %p')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

logger.error("sff")