class SiaDaemon(object):
    """The daemon is responsible for starting and stopping the modules which make up the rest of Sia. It also provides endpoints for viewing build constants."""
    def __init__(self, scpy):
        self.scpy = scpy

    def constants(self):
        """
        Returns the set of constants in use

        :return: Dict with the set of constants in use
        """
        return self.scpy.get_api('/daemon/constants')

    def constant(self, constant):
        """
        Returns a constant from the set of constants in use

        :param constant: The constant to look up
        :type constant: str
        :return: The value of the constant
        :raises: KeyError: if key not in the set of constants
        """
        try:
            return self.scpy.get_api('/daemon/constants')[constant]
        except KeyError:
            pass
        raise KeyError(f"Constant not found: {constant}")


    def stop(self):
        """
        Cleanly shuts down the Sia Daemon

        :return: True if action succeeded, error message if not
        """
        return self.scpy.get_api('/daemon/stop')

    def version(self):
        """
        Returns the version of the Sia Daemon

        :return: String containing the version
        """
        return self.scpy.get_api('/daemon/version')['version']
