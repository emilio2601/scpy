class SiaHostDB(object):
    """
    The HostDB maintains a database of all hosts known to the network. The database identifies hosts by their public key and keeps track of metrics such as price.
    """
    def __init__(self, scpy):
        self.scpy = scpy

    def active(self, numhosts=None):
        if numhosts:
            return self.scpy.get_api('/hostdb/active', params={'numhosts': numhosts})['hosts']
        else:
            return self.scpy.get_api('/hostdb/active')['hosts']

    def all(self):
        return self.scpy.get_api('/hostdb/all')['hosts']

    def host(self, pubkey):
        return self.scpy.get_api(f'/hostdb/hosts/{pubkey}')
