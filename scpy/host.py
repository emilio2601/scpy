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
        """
        Remove a storage folder from the manager. All storage on the folder will be moved to other storage folders, meaning that no data will be lost. If the manager is unable to save data, an error will be returned and the operation will be stopped.

        :param path: Local path on disk to the storage folder to remove.
        :type path: str
        :param force: If true, the storage folder will be removed even if the data in the storage folder cannot be moved to other storage folders, typically because they don't have sufficient capacity. If force is true and the data cannot be moved, data will be lost.
        :type force: bool
        :return: True if action succeeded, error message if not
        """
        return self.scpy.post_api('/host/storage/folders/remove', data={'path': path, 'force': force})

    def resize_folder(self, path, newsize):
        """
        Grows or shrinks a storage folder in the manager. The manager may not check that there is enough space on-disk to support growing the storage folder, but should gracefully handle running out of space unexpectedly. When shrinking a storage folder, any data in the folder that needs to be moved will be placed into other storage folders, meaning that no data will be lost. If the manager is unable to migrate the data, an error will be returned and the operation will be stopped.

        :param path: Local path on disk to the storage folder to resize.
        :type path: str
        :param newsize: Desired new size of the storage folder. This will be the new capacity of the storage folder.
        :type newsize: int
        :return: True if action succeeded, error message if not
        """
        return self.scpy.post_api('/host/storage/folders/resize', data={'path': path, 'newsize': newsize})

    def delete_sector(self, merkleroot):
        """
        Deletes a sector, meaning that the manager will be unable to upload that sector and be unable to provide a storage proof on that sector. This endpoint is for removing the data entirely, and will remove instances of the sector appearing at all heights. The primary purpose is to comply with legal requests to remove data.

        :param merkleroot: Merkle root of the sector to delete.
        :type merkleroot: str
        :return: True if action succeeded, error message if not
        """
        return self.scpy.post_api(f'/host/storage/sectors/delete/{merkleroot}')
