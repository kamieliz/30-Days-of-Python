# Python 30 Day Challenge - Day 1 - Numbers, Arithmetic, & Printing to the Console

# Table of Contents

1. [Brief History of Python](craftdocs://open?blockId=3277565F-948F-4938-AE6D-D3654E829AC8&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
2. [Basic Numbers](craftdocs://open?blockId=29AB62E8-D58A-455C-AFFB-44135B5B44CE&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
3. [The Print function](craftdocs://open?blockId=2D32D5C3-43CB-44C3-83F5-2A455B08DCE7&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
4. [Expressions](craftdocs://open?blockId=73C2C9B8-825D-4663-9B4C-D2B9729ACCB1&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
5. [Arithmetic Operators](craftdocs://open?blockId=438E3AC5-D053-4741-9EAF-6D9107745F34&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Using multiple operators](craftdocs://open?blockId=57FC43AD-5B3C-4263-93FF-3A95CB5C1650&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [Grouping operations with parentheses](craftdocs://open?blockId=730EC592-BDEE-4B1A-B5DE-0D544F2EEA4D&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

## Brief History of Python

- The first version of Python was released 30 years ago in 1990
- One of the main strengths of Python is the readability of its code, which makes it extremely accessible.
- At the time of writing there are two major Python standards in active use
- First we have Python 2.7 which is the most current version of Python 2.
   - Python 2 has technically reached [its end of life](https://www.python.org/doc/sunset-python-2/), and will no longer get any additional updates, but there’s still a huge amount of Python 2 code out there
- The second branch of Python is Python 3, with the most current version being Python 3.9.
   - Python 3 was intended to be a replacement for Python 2, and boasts a number of improvements along with some significant syntax changes.
   - Code written in Python 2 may not be compatible with Python 3, and even if the code runs we may end up with unexpected behaviour

## Basic Numbers

In Python, we have several different ways of representing numbers

- the most common of which are integers and floating point numbers
   - Integers are used to represent whole numbers
      - Creating an integer in Python is very simple: we just have to write an integral number
      - We can also write negative integers by putting a `-` before the number
      - 2, -4, 1000
   - floats are used for real numbers with some decimal component
      - 4.0. -15444.3, 3.141

## The Print function

Python has a built in *function* that outputs things to the console window for us. This function is called `print`

- you can think of functions as bundles of code that we can run to perform some specific action.
- The process of running a function like this is often referred to as “calling” a function
   - `print(4)`
- When we call a function, the parentheses (round brackets) are written directly next to the function name
   - This isn’t going to affect how the code works—Python doesn’t care if we put spaces here—it’s just considered poor style, and developing a good coding style is very important
   - Good style is going to help make your code more readable, which is one of the most important metrics to consider when it comes to writing code

## Expressions

If something in our code evaluates to a value, it’s an expression

- For example, all the integers we've written are expressions. When Python sees each integer, it can use the value they represent.
- We're also about to see some simple arithmetic operations like `5 + 7`, and those operations are expressions too.
   - In the case of `5 + 7`, when Python sees that, it evaluates the expression to another integer: `12`.
- When we write `print()`, that is also a type of expression called a *function call expression*

## Arithmetic Operators

One of the things that we do all the time in Python (and programming in general) is basic arithmetic

- We accomplish this primarily through the use of operator symbols like `+`, `-`, `/`, etc
- when we write `1 + 2`, Python evaluates that and we get an integer with the value `3`
- This is important to keep in mind, because it affects our output when we use something like `print`. If we try to print something like this:
   - `print(1+2)`
   - Python is not going to print out the operation, because by time `print` runs, `1 + 2` has already been evaluated to a single value: the integer, `3`
- if either of the operands for `+` is a float, the expression evaluates to a float. The same is true of several of the other operators, including `-` and `*` (which is used for multiplication)
- Division is performed using the `/` operator, but when performing division the result is *always* a float

### Using multiple operators

Sometimes we need to perform more complicated calculations, and this may involve the use of multiple operators.

- This is totally fine in Python, and we can chain as many of these arithmetic operators together as we like.
- Just make sure that things aren’t becoming hard to read
- Order the expressions are evaluated in corresponds to PEMDAS

### Grouping operations with parentheses

Just like in normal mathematics, we can use parentheses to group operations, and these expressions will be given precedence in the order of evaluation

- When we write binary operators (operators with two operands) like `+`, `-`, and `*`, we should put a space on either side of the operator
- However, it can sometimes be appropriate to forego this space to group operations together
- Grouping the operations in this way helps to remind readers of the order of operations

