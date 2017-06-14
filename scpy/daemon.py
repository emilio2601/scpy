class SiaDaemon(object):
    """The daemon is responsible for starting and stopping the modules which make up the rest of Sia. It also provides endpoints for viewing build constants."""
    def __init__(self, scpy):
        self.scpy = scpy

    def constants(self):
        """
        Returns the set of constants in use

        :returns:  ``dict`` - {'constant': value}
        """
        return self.scpy.get_api('/daemon/constants')

    def constant(self, constant):
        """
        Returns a constant from the set of constants in use

        :param constant: The constant to look up
        :type constant: str
        :returns:  ``str`` - the value of the constant
        :raises: ``KeyError``: If key not in the set of constants
        """
        try:
            return self.scpy.get_api('/daemon/constants')[constant]
        except KeyError:
            pass
        raise KeyError(f"Constant not found: {constant}")


    def stop(self):
        """
        Cleanly shuts down the Sia Daemon

        :returns:  ``bool``: If action was successful
        """
        return self.scpy.get_api('/daemon/stop')

    def version(self):
        """
        Returns the version of the Sia Daemon

        :returns:  ``str``
        """
        return self.scpy.get_api('/daemon/version')['version']
