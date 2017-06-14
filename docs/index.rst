.. toctree::
:caption: scpy api reference
        Daemon <daemon>
        Consensus <consensus>
        Gateway <gateway>
        Host <host>
        HostDB <hostdb>
        Renter <renter>
        Transaction Pool <tpool>
        Wallet <wallet>

scpy
====

Python3 API bindings for the `Sia API <https://github.com/NebulousLabs/Sia/blob/master/doc/API.md>`_

`Sia <http://sia.tech/>`_ is a decentralized cloud storage platform that uses a blockchain to facilitate payments

Usage
-----
    >>> from scpy import Sia
    >>> sc = Sia()
    >>> sc = Sia(host='http://10.0.0.0', port=1234)

By default, scpy connects to the Sia daemon on localhost:9980. You can pass host and/or port as arguments to modify this.

Here are other usage examples:

    >>> sc.wallet.unlock(seed)
    True

    >>> sc.daemon.version()
    '1.2.2'

    >>> sc.consensus()['height']
    109720

    >>> sc.renter.prices()['storageterabytemonth']
    '376439999996419200000000000'

    >>> sc.hastings_to_siacoin(int(sc.renter.prices()['storageterabytemonth']))
    365.0999999969376



Implementation completeness
---------------------------
================== ==== ====== ==========
Module             Done Tested Documented
================== ==== ====== ==========
Daemon             ✔    ✔      ✔
Consensus          ✔    ✔      ✔
Gateway            ✔    ✔      ✖
Host               ✔    ✖      ✖
HostDB             ✔    ✔      ✖
Renter             ✖    ✖      ✖
Transaction Pool   ✔    ✖      ✖
Wallet             ✔    ✖      ✖
================== ==== ====== ==========


Installation
------------

Install scpy by running::

    $ pip install scpy

Contribute
----------
Contributions are really welcome, whether they are bug reports/fixes, new features, documentation writing, really anything is appreciated.

You can send a pull request to our GitHub repo: https://github.com/emilio2601/scpy

Alternatively, open an issue in our bug tracker here: https://github.com/emilio2601/scpy/issues

License
-------
This project is licensed under the GNU GPL v3.0

Donations
---------
    >>> sc.wallet.address()
    81b202b982558b18ef62d93399b34ae0cd5c8e090504fa294d8a6b669a02d88a44caed9ea098
