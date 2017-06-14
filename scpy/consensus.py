class SiaConsensus(object):
    """
    The consensus set manages everything related to consensus and keeps the blockchain in sync with the rest of the network. The consensus set's API endpoint returns information about the state of the blockchain.
    """
    def __init__(self, scpy):
        self.scpy = scpy

    def __call__(self):
        """
        Returns information about the consensus set, such as the current block height.

        :return: dict - a dict with information about the consensus set:
        """
        return self.scpy.get_api('/consensus')
