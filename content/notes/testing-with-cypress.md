---
title: "Testing With Cypress"
---

# Introduction

Cypress allows you to automate the testing of your code. The goal of using a tool like Cypress is to be able to refactor with confidence.

## General Mental Models

- Relying on generic class names or ids is not recomended, instead use what's called a data-attribute in order to do your testing. Data-attributes are not modified in production builds so that is extremely useful.
- Think more about what a user would do
	- Start small and then build up more complicated tests

# Cookbook

## Useful Functions

- `Cy.contains`
- `cy.get` : It gets the cypress test



# Aliases
Aliases are used for us to be able to assign names to regularly accessed document nodes.

## Working with Inputs


# Tasks

## Introduction

We can define tasks in order to do things under the hood which allows us to make some test setup happens