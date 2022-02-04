# Day 13 - Exception Handling and Package Manager

# Table of Contents

1. [Exception Handling](craftdocs://open?blockId=A087B3C6-CBAD-431E-BDAC-103CE6D8ABAD&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Packing and Unpacking arguments in Python](craftdocs://open?blockId=2443E3A4-1114-4DE3-A033-B3BE02B49E5A&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
      1. [Unpacking](craftdocs://open?blockId=885950A3-D64C-4178-B743-3D27A66D02E3&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
      2. [Packing](craftdocs://open?blockId=65575205-59EC-48B6-BA8A-A393548A457D&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [Spreading](craftdocs://open?blockId=DD23CC67-B048-4C4F-B18F-BEF519321877&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   3. [Enumerate](craftdocs://open?blockId=BD00F5F1-568A-4AFD-BDFB-3E53C3AE001C&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   4. [Zip](craftdocs://open?blockId=A375DA03-5587-4311-AF5F-053EC8BDC764&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
2. [Package Manager](craftdocs://open?blockId=8E1422A2-BAEB-4EE2-9F41-11EBEBB56B4D&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# Exception Handling

- python uses try and except to handle errors gracefully
- a graceful exit is when a program detects a serious error condition and exits in a controlled manner as a result
- often the program prints a descriptive error message to a terminal or a log as part of the graceful exit to make the app more robust
- the cause of an exception is often external to the program itself
- examples of exceptions:
   - incorrect input
   - wrong file name
   - unable to find a file
   - malfunctioning IO device

![Image](https://res.craft.do/user/full/d367a179-adcb-7ce8-0b02-ba52d2a7c917/doc/77B863AE-22BA-4099-A0FF-49DFA4713B49/3F323F29-EECF-47A2-AAD2-75ED1308238F_2/Image)

- the correct syntax is below:

```other
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
```

- with except you can specify specific error types to go through

```other
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
```

- can shorten code by using a shortened loop

```other
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
```

## Packing and Unpacking arguments in Python

- use two operators:
   - * for tuples
   - ** for dictionaries

### Unpacking

```other
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

- can unpack using range built in function

```other
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]
```

- unpacking a list

```other
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
```

- unpacking a dictionary

```other
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```

### Packing

- sometimes we never know how many arguments are needed to be passed to a python function
- can use the packing method to allow our function to take unlimited number of arbitrary number of arguments
- packing lists

```other
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

- packing dictionaries

```other
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

## Spreading

```other
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

- built in function to get the index of each item in the list

```other
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

## Zip

- combine lists when looping through them

```other
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

# Package Manager

## What is PIP?

- stands for preferred installer program
- pip is used to install different python packages
- package is a python module that can contain one or more modules or other packages
- a module or modules that we can install to our application is a package

## PIP commands

- install pip using pip
   - `pip install pip`
- check if its installed
   - `pip —version`
- installing packages using pip
   - `pip install <package name>`
   - once installed can use import statements to use in application
- uninstall packages
   - `pip uninstall <package name>`
- to see list of installed packages on machine
   - `pip list`
- show information about package
   - `pip show <package name>`
   - —verbose option can be used to show more detailed information
- to get all the packages used and installed and their version for a requirements file
   - `pip freeze`

## Useful packages

- NumPy - fundamental package for scientific computing in Python
- Web Browser - built in module, helps open any website or schedule that task
- Requests - allows you to open a network connection and implement CRUD (create, read, update, and delete) operations
- SQLAlchemy - object oriented access to several different database systems
- Django - high level web framework
- flask - micro framework for python based on Jinja 2
- BeautifulSoup - HTML/XML parser designed for screen scraping
- PyQuery - implements jQuery in python
- elementTree - flexible container object designed to store hierarchical data structures
- PyQT - bindings for cross platform Qt framework
- TKInter - traditional python user interface toolkit
- Pandas - data analysis, data science and machine learning library
- SciPy - machine learning library
- Scikit-learn - combines NumPy and SciPy for working with complex data

## Creating a package

- packages contain one or more relevant modules
- it is actually a folder containing one or more module files
- package folder contains a special file called init.py that stores the packages content
   - once that is put in a package folder, python starts recognizing it as a package
   - exposes specified resources from its modules to be imported to other python files
   - an empty file makes all functions available when a package is imported

