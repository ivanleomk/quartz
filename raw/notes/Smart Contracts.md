---
title: "Smart Contracts"
---

> Smart contracts are computer programs that live on the blockchain

These programs are immutable and distributed. Therefore they are resistant to tampering and can be used trustlessly. In Etherium, Smart contracts are written using [[Solidity]].

After you deploy a contract to Ethereum, it’s **_immutable_**, which means that it can never be modified or updated again.

The initial code you deploy to a contract is there to stay, permanently, on the blockchain. *This is one reason security is such a huge concern in Solidity*. If there's a flaw in your contract code, there's no way for you to patch it later. You would have to tell your users to start using a different smart contract address that has the fix.

# Contract Problems
## Ownership

We can utilise the concept of ownership in [[Solidity]] in order to ensure that important changes or values that exist within our app can only be changed by specific users.

## Gas
In Solidity, your users have to pay every time they execute a function on your DApp using a currency called **_gas_**. Users buy gas with Ether (the currency on Ethereum), so your users have to spend ETH in order to execute functions on your DApp.

 Each individual operation has a **_gas cost_** based roughly on how much computing resources will be required to perform that operation (e.g. writing to storage is much more expensive than adding two integers). The total **_gas cost_** of your function is the sum of the gas costs of all its individual operations.

Therefore we should look towards [[Solidity Gas Optimization]] as a means to reduce the overall gas cost of our functions for our users


# Resources
- [What are Smart Contracts](https://www.youtube.com/watch?v=ZE2HxTmxfrI)
