import requests as r


class Sia(object):
    def __init__(self, host="http://127.0.0.1", port=9980):
        self.host = host
        self.port = port
        self.daemon = SiaDaemon(self)

    def get_api(self, endpoint, params=None):
        user_agent = {'User-agent': 'Sia-Agent'}
        url = self.host + ":" + str(self.port) + endpoint
        resp = r.get(url, headers=user_agent, params=params)
        return resp.json()

    def post_api(self, endpoint, data=None):
        user_agent = {'User-agent': 'Sia-Agent'}
        url = self.host + ":" + str(self.port) + endpoint
        resp = r.post(url, headers=user_agent, data=data)


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


if __name__ == '__main__':
    sc = Sia()
    print(sc.daemon.version())
