---
title: Typescipt
---

# Overview
> Typescript is an open source, typed syntactic superset of Javascript. It compiles to readable JS

Using typescript, we can write better programs which are easier to edit and refactor down the line.

A good way to think of TS files:

-   `.ts` files contain both type information and code that runs
-   `.js` files contain only code that runs
-   `.d.ts` files contain only type information

# Cookbook

## Functions

We can annote types by

```
function add(a : number, b:number):number {
  return a + b 
}
```

We can also indicate optional parameters by using the `?` operators

```
function add(a: number, b?: number): number {
  if (typeof b === "undefined") {
    return a + 3;
  }
  return a + b;
}
```

We can then use an optional 

## Dictionaries

We can type dictionaries with index signatures

```ts
type phoneBook = {
  [k:string]:{
    country:string
    area:string
    number:string
  }
}
```

## Arrays and Tuples
```ts
const tupl:[number,number,number] = [200,100,300]
```

## Structural vs Nominal Types

> Type-Equivalence : is the type which is passed into the function or returned what we are expected to obtain

Type Systems can either be static or dynamic and this largely has to deal with whether type-checking is performed at compile or runtime. Dynamic type systems perform their type equivalence evaluation at runtime while static type systems do it at compile time.

We also have another differentiator which comes in the form of `Nominal Type Systems` and `Structural Type Systems`.

Nominal Type Systems aim to look at the inheritance pattern of certain clases and whether their names match whereas Structural type systems aim to look at whether the shape and property of the object matches what it is supposed to be.


## Union and Intersection Types
They can conceptually be thought of as logical boolean operators.

```ts
#Union Types
type sampleUnion = "success" | "error"
```

A union type can only exist as a single instance of a category, it's useful to describe mutually exclusive situations. Therefore we can only access common behaviour that is guaranteed if we do not have a type guard.

We can use either

- `instanceOf` to catch cases where we are looking for instances of a class
- `typeof` to ensure we are checking against certain properties/types
- properties of the types that we define

Intersection types on the other hand, help us to create new instances of specific types

```ts
Date & {end:Date}
```


## Type Aliases
> A type alias is useful in helping to define a more meaningful name for a type and declare the different types using a specific alias

```
type UserContactInfo = {
	name:string;
	email:string;
}
```

We can extend existing types by using the `intersection` operator

```
type specialUserContact = userContactInfo & {getUserContact:() => string}
```

## Interfaces
Typescript has both interfaces and classes. A class needs to `implement` an interface while an interface can only `extend` from existing interfaces

```
interface AnimalLike {
  eat(food:string): void
}
 
class Dog implements AnimalLike {
  bark() {
    return "woof"
  }
  eat(food:string) {
    return 
  }
}
```


# Functions and Best Practices
```ts
type addCalc = (x:number,y:number) => number
const add : addCalc = (a,b) => a+b
```

If we have an function which returns an value we might want to ignore, we use a `void` value. If we are confident that it will not return any value at all, then we use the `undefined` keyword

```
function randomFunc():void{
	//doSomething
}
```

