class SiaHost(object):
    """
    The host provides storage from local disks to the network. The host negotiates file contracts with remote renters to earn money for storing other users' files. The host's endpoints expose methods for viewing and modifying host settings, announcing to the network, and managing how files are stored on disk.
    """
    def __init__(self, scpy):
        self.scpy = scpy

    def __call__(self):
        """
        Fetches status information about the host

        :return: Dict with information about the host
        """
        return self.scpy.get_api('/host')

    def set_setting(self, parameter, value):
        """
        Configures hosting parameters.

        :param parameter: The parameter to change, e.g: 'collateral'
        :type parameter: str
        :param value: The parameter's new value
        :return: True if action succeeded, error message if not
        """
        return self.scpy.post_api('/host', data={parameter: value})

    def announce(self, address=None):
        """
        Announce the host to the network as a source of storage. Generally only needs to be called once.

        :param address: The address to be announced. If no address is provided, the automatically discovered address will be used instead.
        :type address: str
        :return: True if action succeeded, error message if not
        """
        if address:
            return self.scpy.post_api('/host/announce', data={'netaddress': address})
        else:
            return self.scpy.post_api('/host/announce')

    def get_folder_list(self):
        """
        Gets a list of folders tracked by the host's storage manager.

        :return: Array of dicts containing each folder and metadata
        """
        return self.scpy.get_api('/host/storage')['folders']

    def add_folder(self, path, size):
        """
        Adds a storage folder to the manager. The manager may not check that there is enough space available on-disk to support as much storage as requested

        :param path: Local path on disk to the storage folder to add
        :type path: str
        :param size: Initial capacity of the storage folder. This value isn't validated so it is possible to set the capacity of the storage folder greater than the capacity of the disk. Do not do this.
        :type size: int
        :return: True if action succeeded, error message if not
        """
        return self.scpy.post_api('/host/storage/folders/add', data={'path': path, 'size': size})

    def remove_folder(self, path, force=False):
        return self.scpy.post_api('/host/storage/folders/remove', data={'path': path, 'force': force})

    def resize_folder(self, path, newsize):
        return self.scpy.post_api('/host/storage/folders/resize', data={'path': path, 'newsize': newsize})

    def delete_sector(self, merkleroot):
        return self.scpy.post_api(f'/host/storage/sectors/delete/{merkleroot}')
