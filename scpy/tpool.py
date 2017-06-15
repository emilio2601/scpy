class SiaTPool(object):
    """
    The transaction pool provides endpoints for getting transactions currently in the transaction pool and submitting transactions to the transaction pool.
    """
    def __init__(self, scpy):
        self.scpy = scpy

    def fee(self):
        return self.scpy.get_api('/tpool/fee')

    def get_raw(self, id):
        return self.scpy.get_api(f'/tpool/raw/{id}')

    def submit_raw(self, parents, transaction):
        return self.scpy.post_api('/tpool/raw', data={'parents': parents, 'transaction': transaction})
