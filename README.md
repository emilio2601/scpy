# scpy
Python3 API bindings for the Sia API

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
|Consensus | |
|Gateway| |
|Host| |
|HostDB| |
|Renter| |
|Transaction Pool| |
|Wallet| Done, not tested |
