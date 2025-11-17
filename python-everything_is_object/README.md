# python-everything_is_object
# Python: Everything is an Object - Understanding Mutable vs Immutable Types

## Introduction

In Python, everything is an object - integers, strings, lists, functions, and even classes themselves. This fundamental concept shapes how Python handles data in memory and affects how we write code. Understanding the difference between mutable and immutable objects is essential for avoiding common bugs and writing efficient Python code. Through hands-on exercises, I explored how Python's object model works, and in this article, I'll share what I learned about object identity, mutability, and how Python passes arguments to functions.

## ID and Type

Every object in Python has three characteristics:
- **Identity**: A unique identifier (memory address) that never changes during the object's lifetime
- **Type**: Defines what operations can be performed on the object
- **Value**: The actual data the object contains

We can inspect these using built-in functions:

