---
title: "Blockchain Mining"
---

# Introduction
Mining is the process that helps create new blocks of transactions to be added to the Ethereum blockchain network. It also helps keep the network secure from attacks.

Every transaction on a blockchain modifies the global state that is replicated across all nodes. Since there are millions of transactions, transactions get grouped together in blocks. Hence the name. These blocks are chained together in a cryptographically verifiable way so they are historically traceable.

Each block stores a hash, the hash of the previous hash and some information. The original use of proof-of-work resulted in it being difficult to create new blocks. As a result, this meant that individuals could not easily modify the state of the blockchain.

> **tldr;**
> 
> Miners create new blocks by using what is known as proof-of-work. This then allows them to propose new blocks to add to the entire network which will then cause the state of the blockchain to be updated across all nodes.


# Miners

> Miners help to keep the network secure by ensuring that transactions are ordered and mantain a certain degree of cohesiveness

In decentralized systems like Ethereum, we need to ensure that everyone in the world agrees on the ordering of transactions.

For example, if Alice sent Bob 1 ETH, which he further sent to Charlie, the order of the transactions NEEDS to be as follows

Alice --> Bob 1 ETH Bob --> Charlie 1 ETH

Any other transaction order will not work, and it is important everyone agrees to this.

Miners, therefore, are also responsible for validating cryptocurrency transactions on the blockchain network and adding them to the ledger.

## How to Mine
Miners need to produce a certificate of legitimacy that all transactions in their proposed block are valid.

Producing this certificate is a computationally hard and complex challenge. This is what all of [[Proof of Work]] is about. We will go more in depth about this in a later tutorial, but for now, just know that producing this certificate is quite hard. 

For the miners hard work in producing these certificates and executing transactions, they are rewarded in the form of new coins. In Ethereum, when a miner successfully mines a block, they receive 2 ETH for their hard work.

## Process
Miners verify a series of transactions and then propose a block to be used. These consist of transactions from their Mempool.

## Mining Pools
Most individual miners do not have enough resources to set up huge mining facilities with thousands of GPUs and ASICs. Mining pools allow miners to combine their computational resources in order to increase their chances of mining blocks. If anyone in the mining pool succeeds at mining a block, the reward is distributed proportionately to everyone in the pool based on their computational power they contribute to the pool.