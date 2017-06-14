import json

class SiaWallet(object):
    def __init__(self, scpy):
        self.scpy = scpy

    def wallet(self):
        return self.scpy.get_api('/wallet')

    def gen_address(self):
        return self.scpy.get_api('/wallet/address')['address']

    def get_addresses(self):
        return self.scpy.get_api('/wallet/addresses')['addresses']

    def backup(self, dest):
        return self.scpy.get_api('/wallet/address', params={'destination': dest})

    def init(self, password, dictionary='english', force=False):
        return self.scpy.post_api('/wallet/init',
                                  data={'encryptionpassword': password, 'dictionary': dictionary, 'force': force})

    def init_with_seed(self, password, seed, dictionary='english', force=False):
        return self.scpy.post_api('/wallet/init/seed',
                                  data={'encryptionpassword': password, 'dictionary': dictionary, 'force': force})

    def add_seed(self, seed, password, dictionary='english'):
        return self.scpy.post_api('/wallet/seed',
                                  data={'encryptionpassword': password, 'dictionary': dictionary, 'seed': seed})

    def get_seeds(self, dictionary='english'):
        return self.scpy.get_api('/wallet/seeds', data={'dictionary': dictionary})

    def send_siacoins(self, amount, destination):
        return self.scpy.post_api('/wallet/siacoins',
                                  data={'amount': amount, 'destination': destination, 'outputs': ""})

    def send_to_many(self, list):
        """list must be an array of (dest, amount) tuples"""
        outputs = []
        for transaction in list:
            outputs.append({'unlockhash': transaction[0], 'value': transaction[1]})
        return self.scpy.post_api('/wallet/siacoins',
                                  data={'amount': "", 'destination': "", 'outputs': json.dumps(outputs)})

    def sweep(self, seed, dictionary='english'):
        return self.scpy.post_api('/wallet/sweep/seed', data={'seed': seed, 'dictionary': dictionary})

    def lock(self):
        return self.scpy.post_api('/wallet/lock')

    def transaction(self, id):
        return self.scpy.get_api(f'/wallet/transaction/{id}')

    def transactions(self, startheight, endheight):
        return self.scpy.get_api('/wallet/transactions', params={'startheight': startheight, 'endheight': endheight})

    def transactions_by_address(self, address):
        return self.scpy.get_api(f'/wallet/transactions/{address}')

    def unlock(self, password):
        return self.scpy.post_api('/wallet/unlock', data={'encryptionpassword': password})

    def is_address_valid(self, address):
        return self.scpy.get_api(f'/wallet/verify/address/{address}')['valid']

    def change_password(self, old, new):
        return self.scpy.post_api('/wallet/changepassword', data={'encryptionpassword': old, 'newpassword': new})
