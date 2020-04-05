
class DeviceDataModel(object):
    class __Init:
        def __init__(self):
            self.val = "Default data"
            self.data_model_file=None
            self.model_data={}


        def __str__(self):
            return repr(self) + self.val

        def read_data(self,data_file_name):
            self.data_model_file=data_file_name=data_file_name
            f = open(data_file_name)
            for line in f.readlines():
                ar=line.split("\t")
                if (len(ar)>2):
                    ar[0]=ar[0].replace(' ','')
                    self.model_data[ar[0]]={}
                    self.model_data[ar[0]]['value']=ar[1]
                    self.model_data[ar[0]]['writeble']=ar[2]
                    self.model_data[ar[0]]['type']=ar[3]


    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not DeviceDataModel.instance:
            DeviceDataModel.instance = DeviceDataModel.__Init()
        return DeviceDataModel.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)