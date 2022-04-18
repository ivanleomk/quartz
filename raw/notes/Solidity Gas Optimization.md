---
title: "Solidity Gas Optimization"
---

# Introduction
We want to minimise the cost of gas to our users because that'll result in a large amount of unneccessary expenses for them otherwise. 

## Using Structs
  
If you have multiple `uint`s inside a struct, using a smaller-sized `uint` when possible will allow Solidity to pack these variables together to take up less storage. For example:

```solidity
struct NormalStruct {
  uint a;
  uint b;
  uint c;
}

struct MiniMe {
  uint32 a;
  uint32 b;
  uint c;
}

// `mini` will cost less gas than `normal` because of struct packing
NormalStruct normal = NormalStruct(10, 20, 30);
MiniMe mini = MiniMe(10, 20, 30); 
```

## Using View Functions

View functions do not need any gas because they do not modify the state of the data. As such, they only require the local etherium node to query the blockchain data. They will however cost gas when they are called inside other functions.

```solidity
function getZombiesByOwner(address _owner) external view returns(uint[] memory) {
    uint[] memory result = new uint[](ownerZombieCount[_owner]);
    // Start here
    return result;
  }
```
