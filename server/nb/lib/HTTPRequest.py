
class HTTPRequest():
    def __init__(self):
        pass
    
    def parse_uri(self,uri):
        ar=uri.split('?')
        ret={
            '_uri_path':ar[0]
        }
        if (len(ar)>1):
            ar2=ar[1].split(";")
            for item in ar2:
                ar3=item.split("=")
                if (len(ar3)>1):
                    ret[ar3[0]]=ar3[1]
        
        return ret
