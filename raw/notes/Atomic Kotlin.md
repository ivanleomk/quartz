---
title: "Atomic Kotlin"
last-updated: "2022-07-18"
---

# Introduction
> Kotlin is a compiled language which is compiled down into Bytecode and is then executed on the [[Java Virtual Machine]].

We can see the basic scaffolding of a Kotlin program such as

```kotlin
fun main() {
    println("Hello, world!!!")
}
```

We can then move on to declaring variables and values. The difference between the two is that **values are immutable while variables are mutable**.

## Types
In Kotlin, we use types as a way to tell Kotlin how to use data. A type provides values from which an expression may be assigned.

Kotlin by default gives us the Types of

- Int
- Double
- Boolean
- String
- Char
- String

We can even specify the type of object we are getting by using different constructors

# Data Structures in Kotlin

## Dictionaries

> In Kotlin, a dictionary is known as a hashMap

We can declare a dictionary by using 

```
val map = hashMapOf<Int, Int>()
```

## Lists

We need to explicitly delcare if we want a mutable or immutable list. If we don't say that we want a mutable list, we won't get one.

```kotlin
listOf(1,2,3) // Immutable
mutableListof(1,2,3) //mutable
```

We can then proceed to add elements by using

- `.add()` : Single item
- `.addAll()` : Entire collection

Useful methods include

- `distinct()` : This returns a List which contains only unique characters


## Sets
> A set is a collection that allows only one element of each value


We can create a set by using the `toSet()` ( List -> Set ) or `setOf` constructor. The following are some useful methods

```kotlin
val intSet = setOf(1, 1, 2, 3, 9, 9, 4)

// No duplicates:
intSet eq setOf(1, 2, 3, 4, 9)

// Element order is unimportant:
setOf(1, 2) eq setOf(2, 1)

// Set membership:
(9 in intSet) eq true
(99 in intSet) eq false

intSet.contains(9) eq true
intSet.contains(99) eq false

// Does this set contain another set?
intSet.containsAll(setOf(1, 9, 2)) eq true

// Set union:
intSet.union(setOf(3, 4, 5, 6)) eq
setOf(1, 2, 3, 4, 5, 6, 9)

// Set intersection:
intSet intersect setOf(0, 1, 2, 7, 8) eq
setOf(1, 2)
```

## Maps

> Maps allow for key-value lookups


Maps are read-only. In order to make them Mutable, we need to delare them as `mutableMapOf`

```kotlin

``` 



# OOP

> Objects are used to hold data and perform actions. An object-oriented languages creates and uses objects


An object has

- Data => These are known as properties
- Actions => Functions it executes using its properties

Here are some specific bits of definitions

- An object is an instance of a class.
- A class is a blueprint of how to construct the object
- A member is a property or function that belongs to an object
- Member Functions : Member functions are functions that only work with specific classes
- We create an instance of an object when we make a val or var of a class

We can define classes by using the `class` keyword

```kotlin
class Computer{
	val color = "Space-Grey"


	fun turnOn(){
		println("Turning On!")
	}

	fun restart(){
	    println("System shutting down....")
	    this.turnOn()
	}
}
```

We can maintain state within a class by defining properties.

- For immutable constants, consider using `vals`, else `vars`
- When we create an object, it is actually a reference to the underlying object.

We can also initialize our classes with specific values by modifying the syntax as seen below

```kotlin
class Computer(
  val name:String,
  val age: Int,
  val brand: String
){


  fun getBrand(){
    println("$brand")
  }

  fun getName(){
    println("$name")
  }

  fun getAge(){
    println("$age")
  }

  fun turnOn(){
		println("Turning On!")
	}

	fun restart(){
	    println("\n\nSystem shutting down....")
      // `This` here is a reference to the specific instance of a Computer
	    this.turnOn()
	}

}
```


We can override specific generic functions such as `toString` so that they work differently for our class

We can then protect specific aspects of our class by using

- public : can be called by client programmers
- private : Only accessible within the class itself




## Useful Kotlin

### Iterating Over a list

```kotlin
nums.forEachIndexed { index, i ->
            // do something
        }
```