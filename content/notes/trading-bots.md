---
title: Trading Bots
---
# Introduction

Notes from my lil foray into automated money making~

> A smart contract is a program that runs on the Ethereum blockchain. It's a collection of code and data that resides at a specific address on the ethereum blockchain. 


Here's a quick [Brownie Cookbook](notes/brownie-cookbook.md) for quick reference. 

We can access information on smart contracts by using the contract explorer. We can then query the balance of specific wallets by using the `balanceOf` function w.r.t that specific token. We can also query this value with respect to the native gas token by using the `balance` function.

# Contract Swaps

We can use the `swapExactTokensForTokens` function using the Uniswap V2 Router contract

```
function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts)
```

It accepts the following arguments:

- An unsigned integer specifying the number of tokens sent to the router
- An unsigned integer specifying the minimum number of tokens expected from the swap
- An array with token contract addresses, starting with the token sent to the router, and ending with the token expected from the swap. This array behaves similar to the array we formed in getAmountsOut(), and will require all intermediate wrapper tokens to be passed.
- An address for the destination of the output tokens. This is typically set to match the user calling for the swap, but could be set to an alternative address.
- An unsigned integer representing the deadline for the swap in UNIX format. UNIX formatted deadline represent the number of seconds that have passed since the epoch (midnight on January 1, 1970). This is an internal “safety” mechanism in the contract — the Router contract will not execute the swap if the current block time has exceeded the deadline, which can protect you if the swap lingers in the mempool for an excessive time. By that time, your expected swap may no longer be profitable.

# Concepts

## Slippage

Slippage is commonly described as the allowed price difference between the submitted swap and the executed swap. Common recommendations are to set the slippage to 0.5% - 1% for normal pairs, and up to 5% on low volume pairs.