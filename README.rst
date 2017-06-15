scpy
====

Python3 bindings for the `Sia API <https://github.com/NebulousLabs/Sia/blob/master/doc/API.md>`_

`Sia <http://sia.tech/>`_ is a decentralized cloud storage platform that uses a blockchain to facilitate payments

Usage
-----

.. code-block:: python

    >>> from scpy import Sia
    >>> sc = Sia()
    >>> sc = Sia(host='http://10.0.0.0', port=1234)

By default, scpy connects to the Sia daemon on localhost:9980. You can pass host and/or port as arguments to modify this.

scpy has 8 modules, which have their own methods. The documentation for each of those modules can be accessed in the
sidebar. Here is an example of usage for each module:

.. code-block:: python

    >>> sc.daemon.version()
    '1.2.2'

    >>> sc.consensus()['height']
    109720

    >>> sc.gateway.connect('12.34.56.78:9981')
    True

    >>> sc.host()['externalsettings']['acceptingcontracts']
    False

    >>> sc.hostdb.active()
    [{'acceptingcontracts': True, 'maxdownloadbatchsize': 17825792, 'maxduration': 25920, ...}, ...]

    >>> sc.renter.prices()['storageterabytemonth']
    '376439999996419200000000000'

    >>> sc.tpool.fee()
    {"minimum": "1234", "maximum": "5678"}

    >>> sc.wallet.get_addresses()
    ['81b202b982558b18ef62d93399b34ae0cd5c8e090504fa294d8a6b669a02d88a44caed9ea098', ...]



Implementation completeness
---------------------------
================== ==== ====== ==========
Module             Done Tested Documented
================== ==== ====== ==========
Daemon             ✔    ✔      ✔
Consensus          ✔    ✔      ✔
Gateway            ✔    ✔      ✔
Host               ✔    ✖      ✖
HostDB             ✔    ✔      ✖
Renter             ✔    ✖      ✖
Transaction Pool   ✔    ✖      ✖
Wallet             ✔    ✖      ✖
================== ==== ====== ==========


Installation
------------

.. code-block:: console

    $ pip install scpy

Contribute
----------
Contributions are really welcome, whether they are bug reports/fixes, new features, documentation writing, really anything is appreciated.

You can send a pull request. Alternatively, open an issue in our bug tracker here: https://github.com/emilio2601/scpy/issues

Documentation
----------
It's a WIP (refer to completeness table) but some modules are already finished. Access it here: https://scpy.readthedocs.io/en/latest/

License
-------
This project is licensed under the GNU GPL v3.0

Donations
---------
.. code-block:: python

    >>> sc.wallet.gen_address()
    81b202b982558b18ef62d93399b34ae0cd5c8e090504fa294d8a6b669a02d88a44caed9ea098
