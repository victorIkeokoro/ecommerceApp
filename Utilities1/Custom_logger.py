import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:/Users/Hugo-Tech-1775/Desktop/ecommerce_app/Logs/automation_log.log",
                            format="%(asctime)s: %(levelname)s: %(message)s")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

