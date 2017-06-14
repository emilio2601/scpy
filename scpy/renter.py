class SiaRenter(object):
    def __init__(self, scpy):
        self.scpy = scpy

    def prices(self):
        return self.scpy.get_api('/renter/prices')
