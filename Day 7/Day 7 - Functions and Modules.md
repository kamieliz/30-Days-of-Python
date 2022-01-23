# Day 7 - Functions and Modules

# Table of Contents

1. [Functions](craftdocs://open?blockId=A9A751F0-A2CE-4F83-AB23-5081A9AEEA47&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Defining a Function](craftdocs://open?blockId=681B74DF-5B22-480C-A7DF-84DF89DC3C3D&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
2. [Modules](craftdocs://open?blockId=6DE59B79-2EAC-433C-B3D3-C9FA8C97B846&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Built-in Modules](craftdocs://open?blockId=23982BC7-FBBE-4298-8B33-596AC44B8F2D&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# Functions

## Defining a Function

- a function is a reusable block of code or programming statements designed to perform a certain task
- to define or declare a function use the def keyword
- the function block of code is executed only if the functions is called or invoked.
- when making a function, we call it declaring a function
- when its used its called calling or invoking a function
- can be declared with or without parameters
- functions can also return values,
   - if a function does not have a return statement, the value of the function is None
- in a function we can pass different data types (number, string, boolean, list, tuple, dictionary or set) as a parameter

```other
# declaring a function
def function_name():
		codes
		codes

# calling a function
function_name()
```

- if your function takes one or more parameters in the declaration then you need to include them as arguments when you call the function

```other
def function_name(parameter)
		codes
		codes

print(function_name(argument))
```

- if we pass the arguments with key and value, the order of the argument does not matter

```other
def function_name(para1, para2):
		codes
		codes

print(function_name(para1 = 'John', para2 = 'Doe'))
```

- to return a value with a function we use the keyword return followed by the variable we are returning.
   - can return any kind of data type
- you can pass default values to parameters, when the function is invoked
   - if you do not pass arguments when calling the function, their default values will be used.

```other
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

- if we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name

```other
def function_name(*args):
		codes
		codes

function_name(param1, param2, param3,..)
```

- Can mix default and arbitrary number of parameters in functions

```other
def generate_groups(team, *args):
		print(team)
		for i in args:
				print(i)
print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob')
```

- Can use functions as a parameter of another function

```other
def square_number(n):
		return n * n
def do_something(f, x):
		return f(x)
print(do_something(square_number, 3))
```

# Modules

- a module is a file containing a set of codes or a set of functions which can be included to an application
- could be a file containing a single variable, a function or a big code base
- to create a module, write our codes in a python script and save it as a .py file
   - create the file inside your project folder
   - import the module in your main script
- to import a module, use the import keyword and the name of the file only
   - `import mymodule`
- can import specific functions from a module
   - `from mymodule import function1, function2`
- can rename module when importing
   - `import mymodule as mm`
- Can import modules by importing the file/function using the key word import

## Built-in Modules

- Some of the common built-in modules:
   - math
   - datetime
   - os
   - sys
   - random
   - statistics
   - collections
   - json
   - re
- **OS modul**e makes it possible to automatically perform many system tasks
   - provides functions for creating, changing current working directory, removing a directory, fetching its contents, changing and identifying the current directory

```other
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

- **Sys module** provides functions and variables used to manipulate different parts of the python runtime environment
   - returns a list of command line arguments passed to a python script
   - the item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line

```other
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

   - **statistics module** provides functions for mathematical statistics of numeric data
      - defined as mean, median, mode, stdev

```other
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

   - **math module** contains many mathematical operations and constants

```other
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
```

   - a **string module** is useful for many purposes

```other
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

   - **random module** gives us a random number between 0 and 0.9999
      - has lots of functions but the most common are random and randint

```other
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
```

