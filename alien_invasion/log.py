import logging
from settings import Settings

class Log():
    def __init__(self, name='debug'):
        self.settings = Settings()
        if self.settings.debug == False:
            return
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(name)
    
    def info(self, msg):
        if self.settings.debug == False:
            return
        self.logger.info(msg)