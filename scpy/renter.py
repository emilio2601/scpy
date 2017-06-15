class SiaRenter(object):
    def __init__(self, scpy):
        self.scpy = scpy

    def __call__(self):
        return self.scpy.get_api('/renter')

    def set_setting(self, parameter, value):
        return self.scpy.post_api('/renter', data={parameter: value})

    def get_contracts(self):
        return self.scpy.get_api('/renter/contracts')['contracts']

    def downloads(self):
        return self.scpy.get_api('/renter/downloads')['downloads']

    def files(self):
        return self.scpy.get_api('/renter/files')['files']

    def prices(self):
        return self.scpy.get_api('/renter/prices')

    def delete(self, path):
        return self.scpy.post_api(f'/renter/delete/{path}')

    def download(self, path, dest, async=True):
        if async:
            return self.scpy.get_api(f'/renter/downloadasync/{path}', params={'destination': dest})
        else:
            return self.scpy.get_api(f'/renter/download/{path}', params={'destination': dest})

    def rename(self, old, new):
        return self.scpy.post_api(f'/renter/rename/{old}', data={'newsiapath': new})

    def upload(self, path, source, datapieces, paritypieces):
        return self.scpy.post_api(f'/renter/upload/{path}', data={'datapieces': datapieces, 'paritypieces': paritypieces, 'source': source})