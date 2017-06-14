class SiaGateway(object):
    def __init__(self, scpy):
        self.scpy = scpy

    def __call__(self):
        return self.scpy.get_api('/gateway')

    def connect(self, address):
        return self.scpy.post_api(f'/gateway/connect/{address}')

    def disconnect(self, address):
        return self.scpy.post_api(f'/gateway/disconnect/{address}')
