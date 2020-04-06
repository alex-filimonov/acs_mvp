
import sys

class HTTPRequest():
    def __init__(self):
        pass
    
    def parse_uri(self,uri):
        ar=uri.split('?')
        ret={
            '_uri_path':ar[0]
        }
        if (len(ar)>1):
            ar2=ar[1].split("&")
            for item in ar2:
                ar3=item.split("=")
                if (len(ar3)>1):
                    ret[ar3[0]]=ar3[1]
        
        return ret

    def parse_environ(self,environ):
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size)
        ret={}
        ar=request_body.decode().split('&')
        for item in ar:
            ar2=item.split("=")
            if (len(ar2)>1):
                ret[ar2[0]]=ar2[1]

        return ret
