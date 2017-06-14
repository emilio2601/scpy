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
