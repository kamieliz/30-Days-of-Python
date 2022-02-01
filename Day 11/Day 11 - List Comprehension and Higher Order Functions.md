# Day 11 - List Comprehension and Higher Order Functions

# Table of Contents

# List Comprehension

- a compact way of creating a list from a sequence
- short way to create a new list
- considerably faster than processing a list using the for loop

```other
# syntax
[i for i in iterable if expression]
```

- can be used to change a string to a list of characters

```other
language = 'Python'
lst = [i for i in language]
print(lst) # ['P', 'y', 't', 'h', 'o', 'n']
```

- can generate a list of numbers

```other
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

- can be combined with if expression

```other
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Lambda Function

- small anonymous function without a name
- can take any number of arguments, but can only have one expression
- similar to anonymous functions in JavaScript
- can write lambda functions inside another function

```other
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
```

- create a lambda function using lambda keyword followed by a parameter(s) followed by an expression

```other
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

# Higher Order Functions

- In python, functions are treated as first class citizens, allowing you to perform the following operations on functions:
   - a function can take one or more functions as parameters
   - a function can be returned as a result of another function
   - a function can be modified
   - a function can be assigned to a variable

### Function as a Parameter

```other
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Function as a Return Value

```other
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square') # returns different functions based on param
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

## Python Closures

- Python allows a nested function to access the outer scope of the enclosing function, known as a closure
- created by nesting a function inside another encapsulating function and then returning the inner function

```other
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Python Decorators

- a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure
- called before the definition of a function you want to decorate
- need an outer function with an inner wrapped function to create a decorator function
- can apply multiple decorators to a single function
- decorator functions can take parameters

## Built in Higher order functions

- map(), filter and reduce are built in higher order functions
- the best use case of lambda functions are in functions like map, fileter and reduce

### Map function

- takes a function and iterable as parameters
- map iterates over a list and applies the function to each element

```other
# syntax
map(function, iterable)

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

### Filter function

- calls the specified function when returns boolean for each item of the specified iterable
- filters the items that satisfy the filtering criteria

```other
# syntax
filter(function, iterable)

# Lets filter only even numbers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

### Reduce Function

- defined in the functools module which needs to be imported to use reduce
- takes two parameters, a function and an iterable
- does not return another iterable, instead it returns a single value

```other
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

