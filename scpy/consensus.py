class SiaConsensus(object):
    def __init__(self, scpy):
        self.scpy = scpy

    def __call__(self):
        return self.scpy.get_api('/consensus')
