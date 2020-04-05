
import configparser
import logging
import lib.RedisProvider as RedisProvider



class Init(object):
    class __Init:
        def __init__(self):
            self.config_file=None
            self.config=configparser.ConfigParser()
            self.database=None
            self.mode="simple"
            self.redis=RedisProvider.RedisProvider()


        def __str__(self):
            return repr(self) + self.val

        def read_config(self):
            dataset=self.config.read(self.config_file)
            if len(dataset)<1:
                raise Exception("Config file not found:"+self.config_file)

            # инициируем логер
            logging.basicConfig(format = u'{ level="%(levelname)-8s", time="[%(asctime)s]", message="%(message)s"}', level = int(self.config['DEFAULT']['log_level']), filename = self.config['DEFAULT']['log_file'])
            logging.info (u'Logging is init.....' )

        def get_acs_url(self):
            return self.config['DEVICE']['acs_url']

        def get_sn(self):
            return self.config['DEVICE']['sn']
        
        def log_error(self,str):
            logging.error (str)
        def log_info(self,str):
            logging.info (str)
        def log_debug(self,str):
            logging.debug (str)



    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Init.instance:
            Init.instance = Init.__Init()
        return Init.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)