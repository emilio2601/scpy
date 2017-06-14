# scpy
Python3 API bindings for the [Sia API](https://github.com/NebulousLabs/Sia/blob/master/doc/API.md)

[Sia](http://sia.tech/) is a decentralized cloud storage platform that uses a blockchain to facilitate payments

# Usage
```python
>>> sc = Sia() #by default it connects to localhost:9980
>>> sc = Sia(host='http://10.0.0.0', port=1234)

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

```

# Implementation completeness
| Module      | Done?      |
| ------------- |:-------------:|
|Daemon| Done, tested |
|Consensus | Done, tested |
|Gateway| Done, tested |
|Host| |
|HostDB| Done |
|Renter| |
|Transaction Pool| Done |
|Wallet| Done, not tested |

# Contributing
Contributions are really welcome, whether they are bug reports/fixes, new features, documentation writing, really anything is appreciated.

# License
This project is licensed under the GNU GPL v3.0

# Donations
```python
>>> sc.wallet.address()
81b202b982558b18ef62d93399b34ae0cd5c8e090504fa294d8a6b669a02d88a44caed9ea098
```
