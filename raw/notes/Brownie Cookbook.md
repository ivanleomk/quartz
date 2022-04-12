---
title: Brownie Cookbook
---

# Basic

- Loading Dev Console : `brownie console --network <network_name>`


```
(virtual) ivanleo@Ivans-MacBook-Pro degen % brownie console --network avax-main
Brownie v1.18.1 - Python development framework for Ethereum

No project was loaded.
Brownie environment is ready.
>>> user = accounts.load("test_account")
Enter password for "test_account": 
```

- Load smart contract : `Contract.from_explorer(<explorer Name>`

```
>>> wavax_contract = Contract.from_explorer('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')
```


## Smart Contract Workarounds

We can calculate the value of a smart contract's balance by using

```
amount / (10**contract.decimals())
```
We can

## DEX Operations

1. getAmountsOut



```

```