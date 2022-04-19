---
title: "Gas"
---

> Gas is the fuel that allows it (Ethereum) to operate, in the same way that a car needs gasoline to run.


Just like how seconds are a unit of time, and metres a unit of distance, gas by itself is a unit of computation on the Ethereum Network. The gas unit is used to measure the amount of computational effort required to execute a transaction on Ethereum. Since each transaction requires some computation resources to execute, it requires a fee, commonly called Gas fees or Transaction fees.


In addition to user specified gas limits per transaction, the Ethereum network also imposes a limit on the maximum amount of gas (units) allowed in a single block.

## Pre London
> Original Formula : `gas fees = gas spent * gas price`

Gas Spent is the total amount of gas (in gas units) that were used to execute the transaction
Gas Price is the amount of ether you're willing to pay per gas unit of execution

## Post London
On August 5th, 2021 - the London Upgrade was implemented on the Ethereum network. This upgrade primarily introduced three benefits:

- Better gas fees estimations
- Quicker transaction inclusion
- Burning a percentage of ETH being used as transaction fees

 Since Ethereum does not have an overall maximum supply (unlike Bitcoin, which has a maximum supply of 21M Bitcoins), the burn helps the ETH supply reach an equilibrium by not inflating it infinitely.

In addition to the base fees, the concept of tipping (priority fees) was introduced. As the base fees got burnt, the tip was there to compensate miners for executing and propogating user transactions. This is again set by most wallets automatically, though you can choose to set this manually. Higher tip transactions tend to get higher priority.

> New Formula : `gas spent  * (base fees + priority fees)`

### Variable Block Size

The upgrade introduced variable size blocks to Ethereum. Each block now has a target gas limit of 15M gas, but the size can increase or decrease along with network demand, up until a maximum of 30M gas.

## Rationale for Gas
Gas fees help keep the Ethereum network secure. By requiring a fee for every computation executed on the network, bad actors are prevented from spamming the network.

In order to avoid accidental or malicious infinite loops in smart contracts, which would cause all Ethereum nodes to forever be stuck, gas limits on transactions set a limit to how much computation a transaction can use.