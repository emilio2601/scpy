class SiaHost(object):
    """
    The host provides storage from local disks to the network. The host negotiates file contracts with remote renters to earn money for storing other users' files. The host's endpoints expose methods for viewing and modifying host settings, announcing to the network, and managing how files are stored on disk.
    """
    def __init__(self, scpy):
        self.scpy = scpy

    def __call__(self):
        return self.scpy.get_api('/host')

    def set_setting(self, parameter, value):
        return self.scpy.post_api('/host', data={parameter: value})

    def announce(self, address=None):
        if address:
            self.scpy.post_api('/host/announce', data={'netaddress': address})
        else:
            self.scpy.post_api('/host/announce')

    def get_folder_list(self):
        return self.scpy.get_api('/host/storage')['folders']

    def add_folder(self, path, size):
        return self.scpy.post_api('/host/storage/folders/add', data={'path': path, 'size': size})

    def remove_folder(self, path, force=False):
        return self.scpy.post_api('/host/storage/folders/remove', data={'path': path, 'force': force})

    def resize_folder(self, path, newsize):
        return self.scpy.post_api('/host/storage/folders/resize', data={'path': path, 'newsize': newsize})

    def delete_sector(self, merkleroot):
        return self.scpy.post_api(f'/host/storage/sectors/delete/{merkleroot}')
