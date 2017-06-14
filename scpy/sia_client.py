import pprint

import requests as r


class Sia(object):
    def __init__(self, host="http://127.0.0.1", port=9980, unit='siacoin'):
        self.url = host + ":" + str(port)
        self.daemon = SiaDaemon(self)
        self.consensus = SiaConsensus(self)
        self.gateway = SiaGateway(self)
        self.host = SiaHost(self)
        self.hostdb = SiaHostDB(self)
        self.renter = SiaRenter(self)
        self.tpool = SiaTPool(self)
        self.wallet = SiaWallet(self)



    def get_api(self, endpoint, params=None):
        user_agent = {'User-agent': 'Sia-Agent'}
        resp = r.get(self.url + endpoint, headers=user_agent, params=params)
        return resp.json()

    def post_api(self, endpoint, data=None):
        user_agent = {'User-agent': 'Sia-Agent'}
        resp = r.post(self.url + endpoint, headers=user_agent, data=data)
        return resp.json()

    def hastings_to_siacoin(self, hastings):
        return hastings / 1000000000000000000000000


class SiaDaemon(object):
    def __init__(self, scpy):
        self.scpy = scpy

    def constants(self, constant=None):
        return self.scpy.get_api('/daemon/constants')

    def constant(self, constant):
        try:
            return self.scpy.get_api('/daemon/constants')[constant]
        except KeyError:
            pass
        raise KeyError(f"Constant not found: {constant}")

    def stop(self):
        return self.scpy.get_api('/daemon/stop')

    def version(self):
        return self.scpy.get_api('/daemon/version')['version']


class SiaConsensus(object):
    def __init__(self, scpy):
        self.scpy = scpy


class SiaGateway(object):
    def __init__(self, scpy):
        self.scpy = scpy


class SiaHost(object):
    def __init__(self, scpy):
        self.scpy = scpy


class SiaHostDB(object):
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


class SiaRenter(object):
    def __init__(self, scpy):
        self.scpy = scpy

    def prices(self):
        return self.scpy.get_api('/renter/prices')


class SiaTPool(object):
    def __init__(self, scpy):
        self.scpy = scpy


class SiaWallet(object):
    def __init__(self, scpy):
        self.scpy = scpy

if __name__ == '__main__':
    sc = Sia()
    pprint.pprint(sc.hostdb.host("ed25519:34db39ec43b507a415d3ca57348737bad6ee9725a00561a7f4ca1b25251dd7d3"))
