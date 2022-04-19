---
title: "Proof of Work"
---

> Ethereum, like Bitcoin, currently uses a consensus protocol called Proof of Work (PoW). This allows all nodes on the Ethereum Network to agree on the current state of the blockchain, and secures the network against a variety of attacks.

# Introduction
Under Proof of Work, [[Blockchain Mining]] requires that miners in the network compete against each other to create new blocks full of processed transactions. This new block is then shared with the rest of the network and the winner to broadcast this transaction first earns freshly minted ETH for its hard work.

The race is won by whoever's computer can solve a computationally hard mathematical puzzle the fastest. The problem is computationally hard to solve, but very easy to verify. The solution to this problem is the 'certificate of legitimacy' we discussed in the What is Mining? tutorial.

## Rationale
  
Proof of Work protects against Sybil attacks by making miners put up a large amount of computational power as collateral, therefore having them expend a lot of electrical energy. This is done through the solving of the computation puzzle to prove that the miners are 'putting in the work'. This acts as an economic deterrent to Sybil attacks.

## Work
Essentially, we want to prove that the miners expended energy and computational power to compute the block. And, that they did so faster than everyone else. If we can prove this, it means that the miner essentially spent money and time (in the form of energy and computation) so they could get a chance to propose a new block.

The Ethereum proof-of-work protocol, Ethash, requires miners to go through an intense race of trial and error. The process goes as follows:

- Miner selects a group of transactions to include in a block
- The network then makes the miner to create a slice of data from the state of the network
- This slice is then put through a hash to calculate a target value
- Miners then try to use a combination of the target dataset, nonce and a couple of other values to find a number that is lower than the target
  
  `HashFunction(dataset,target, nonce,...) = desired Value`
- Miners keep using trial-and-error to find a valid value for the nonce which satisfies this condition.
