---
title: "Solidity"
---

# Initialising A Program

We initialise a program by defining the compiler version and then initialising contracts

```solidity
// Define the compiler version you would be using
pragma solidity ^0.8.10;

// Start by creating a contract named HelloWorld
contract HelloWorld {

}
```

# Variables

## Variable Storage
In solidity we have two kinds of storage for our variables, `Storage` and `Memory`. Storage refers to variables stored permanently on the blockchain. Memory variables are temporary, and are erased between external function calls to your contract. Think of it like your computer's hard disk vs RAM.

State variables (declared outside contracts) are by default `Storage` and variables declared inside functions are by default `Memory` type.

## Generic Values
We can initialise variables by simply declaring them. Sample variables types include
- `uint`

## Structs
We can also create structs which will allow us to be able to create objects that have their own unique properties

```solidity
struct Zombie {
	string name;
	uint dna;
}
```

## Arrays
Solidity supports two kinds of arrays, dynamic and static arrays

```solidity
// Array with a fixed length of 2 elements:
uint[2] fixedArray;

// another fixed Array, can contain 5 strings:
string[5] stringArray;

// a dynamic Array - has no fixed size, can keep growing:
uint[] dynamicArray;
```

We can also for instance create an array of structs

```solidity
Zombie[] zombies;
```

# Functions
Well, there are two ways in which you can pass an argument to a Solidity function:

- `By value` : Create a copy of the parameter's value and pass to the function. Our function then modifies the value wtihout modifying the initial parameter
- `By Reference` : Our function takes a reference of the parameter. Any changes to the parameter will therefore be reflected

We can declare a function as seen below. Note that all functions are public by default. We can delcare a function as private by using the `private` key word.

```solidity
function _createZombie(string memory _name, uint _dna) private {
    zombies.push(Zombie(_name, _dna));
}
```

## View Functions
We can also declare our 

So in this case we could declare it as a **_view_** function, meaning it's only viewing the data but not modifying it:

```solidity
function sayHello() public view returns (string memory) {
```


## Return Types
To return a value from a function, the declaration looks like this:

```solidity
string greeting = "What's up dog";

function sayHello() public returns (string memory) {
  return greeting;
}
```

In Solidity, the function declaration contains the type of the return value (in this case `string`).

## Calling Other Functions
We can call other functions by performing

```solidity
function createRandomZombie(string memory _name) public {
	uint randDna = _generateRandomDna(_name);
	_createZombie(_name, randDna);
}
```

We can deal with multiple return types as seen below

```solidity
function multipleReturns() internal returns(uint a, uint b, uint c) {
  return (1, 2, 3);
}

function processMultipleReturns() external {
  uint a;
  uint b;
  uint c;
  // This is how you do multiple assignment:
  (a, b, c) = multipleReturns();
}

// Or if we only cared about one of the values:
function getLastReturnValue() external {
  uint c;
  // We can just leave the other fields blank:
  (,,c) = multipleReturns();
}
```

## Function Invariants

We can also specify function invariants which must be adhered to by using the `require` keyword. This allows us to ensure that specific invariants are followed before any changes are applied to the mutated state of our smart contract.

```solidity
function createRandomZombie(string memory _name) public {
	require(ownerZombieCount[msg.sender] == 0);
	uint randDna = _generateRandomDna(_name);
	_createZombie(_name, randDna);
}
```

## Events

**_Events_** are a way for your contract to communicate that something happened on the blockchain to your app front-end, which can be 'listening' for certain events and take action when they happen.

We can first define events by doing

```solidity
event NewZombie(uint zombieId, string name, uint dna);
```

and then emit and event on the blockchain by performing the function call of

```solidity
emit NewZombie(id, _name, _dna);
```

 

# Inheritance
Solidity supports inheritance and this allows us to perform inheritance when we have multiple contracts.

```solidity
contract ZombieFeeding is ZombieFactory {
	//Contract Goes Here
}
```

## Interfaces
We can also specify interfaces such that the compiler knows how to call specific functions which might not be defined in it's source code as seen below

```solidity
contract KittyInterface {
  function getKitty(uint256 _id) external view returns (
    bool isGestating,
    bool isReady,
    uint256 cooldownIndex,
    uint256 nextActionAt,
    uint256 siringWithId,
    uint256 birthTime,
    uint256 matronId,
    uint256 sireId,
    uint256 generation,
    uint256 genes
  );
}
```

This is useful when we want to reference contracts which are deployed on the blockchain but not in our source code as seen below

```solidity
contract ZombieFeeding is ZombieFactory {

  address ckAddress = 0x06012c8cf97BEaD5deAe237070F9587f8E7A266d;
  KittyInterface kittyContract = KittyInterface(ckAddress);
	
  // Other Stuff

}
```