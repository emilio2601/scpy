from scpy import Sia

class SiaHost(object):
    def __init__(self, scpy: Sia):
        self.scpy = scpy

    def __call__(self):
        self.scpy.get_api('/host')

    def set_setting(self, parameter, value):
        self.scpy.post_api('/host', data={parameter: value})

    def announce(self, address=None):
        if address:
            self.scpy.post_api('/host/announce', data={'netaddress': address})
        else:
            self.scpy.post_api('/host/announce')

    def get_folder_list(self):
        self.scpy.get_api('/host/storage')['folders']

    def add_folder(self, path, size):
        self.scpy.post_api('/host/storage/folders/add', data={'path': path, 'size': size})

    def remove_folder(self, path, force=False):
        self.scpy.post_api('/host/storage/folders/remove', data={'path': path, 'force': force})

    def resize_folder(self, path, newsize):
        self.scpy.post_api('/host/storage/folders/resize', data={'path': path, 'newsize': newsize})

    def delete_sector(self, merkleroot):
        self.scpy.post_api(f'/host/storage/sectors/delete/{merkleroot}')
