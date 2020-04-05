
import configparser
import logging
import lib.DeviceDataModel as DeviceDataModel


class Init(object):
    class __Init:
        def __init__(self):
            self.val = "Default data"
            self.config_file=None
            self.config=configparser.ConfigParser()
            self.database=None
            self.mode="simple"
            self.coockie=None

        def __str__(self):
            return repr(self) + self.val

        def read_config(self,line_arg_parser):
            dataset=self.config.read(self.config_file)
            if len(dataset)<1:
                raise Exception("Config file not found:"+self.config_file)

            deviceDataModel=DeviceDataModel.DeviceDataModel()
            deviceDataModel.read_data(self.config['DEVICE']['model_data_file'])

            args = line_arg_parser.parse_args()
            if args.sn!=None:
                self.config['DEVICE']['sn']=args.sn
                deviceDataModel.model_data['InternetGatewayDevice.DeviceInfo.SerialNumber']['value']=args.sn

            if args.acs_url!=None:
                self.config['DEVICE']['acs_url']=args.acs_url
            if args.periodic_inform_interval!=None:
                self.config['DEVICE']['periodic_inform_interval']=args.periodic_inform_interval
            # инициируем логер
            logging.basicConfig(format = u'{ level="%(levelname)-8s", time="[%(asctime)s]", message="%(message)s"}', level = int(self.config['DEFAULT']['log_level']), filename = self.config['DEFAULT']['log_file'])
            logging.info (u'Logging is init.....' )

        def get_acs_url(self):
            return self.config['DEVICE']['acs_url']

        def get_sn(self):
            return self.config['DEVICE']['sn']
        
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