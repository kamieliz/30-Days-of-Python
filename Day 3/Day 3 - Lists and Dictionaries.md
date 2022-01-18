# Day 3 - Lists and Dictionaries

# Table of Contents

1. [Lists](craftdocs://open?blockId=880C6BDA-292D-4CBC-BFCD-4757A9C47776&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [How to create a list](craftdocs://open?blockId=580CFFFB-3841-450D-AE73-AE4289337067&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [Indexing](craftdocs://open?blockId=164C7988-1264-4CDA-8456-49B3709AC2C6&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   3. [Modifying Lists](craftdocs://open?blockId=BED54717-3704-4E5D-BD6C-6113F2C4691B&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   4. [List Analysis](craftdocs://open?blockId=6778B476-AAB2-4351-AC04-7196F6F5DCB1&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
2. [Dictionaries](craftdocs://open?blockId=1F5550B2-9ADA-4D9D-B0E9-D08FC1CB9350&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Creating a dictionary](craftdocs://open?blockId=7FF7BF6C-0E9C-4150-875E-D9A3E3AA4879&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [Modifying dictionaries](craftdocs://open?blockId=7173676E-13A4-407D-B2FF-87B6118CF561&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# Lists

There are four collection types in Python:

- Lists - a collection which is ordered and modifable
   - allow for duplicate members
- Tuple - a collection which is ordered and unmodifiable (immutable)
   - allows for duplicates
- Set - a collection that is unordered, can't be indexed, unmodifiable
   - allows you to add new items
   - does not allow duplicates
- Dictionary - a collection which is unordered, modifiable and indexed
   - doesn’t allow duplicates

## How to create a list

- lists can be empty or have different data types inside
- Can create lists two ways:
   - using list built in function
   - using square brackets
- the **len()** function allows you to find the length of a list

## Indexing

- Can access each item in a list using their index
- a list index starts from 0
- max index is always the length of a list minus 1
- negative indexing means beginning from the end,
   - \-1 refers to the last item
   - \-2 refers to the second last item
- Can slice items form a list using indexing
   - positive indexing: can specify a range of positive indexes by specifying the start, end, and step
      - this returns a new list
      - default values for start = 0, end = len(list) - 1 and step = 1
      - is not inclusive of the last value in slice
   - negative indexing: can specify a range of negative indexes specifying start, end and step

## Modifying Lists

- since lists are mutable that means you can add and remove items
- to check if an item is in a list use the in operator
- to add items to a list use the **append()** method
- to change specific indexes call the **list[index]** and set it equal to the new value
- to insert items in a list use the **insert()** method to insert at a specific index
   - other items are shifted to the right
   - method takes two arguments: index and an item to insert
- can remove items in three ways:
   - **remove()** method takes the item(s) you want to remove as an argument
   - **pop()** removes a specified index or the last item if index isnt specified
   - **del** keyword removes the specified index and it can also be used to delete items within index range
- to empty or clear a list completely:
   - use del keyword with list
   - **clear()** method
- use the **copy()** method to create a copy without modifying the original
- Can join or concatenate two or more lists:
   - use plus operator
   - use **extend()** method
- can count the number of times an item appears in a list using **count()**
- The **index()** method returns the index of an item in a list
- **reverse()** reverses the order of a list
- **sort()** modifies the original list when it reorders the list
- **sorted()** sorts the list without modifying the original list

## List Analysis

- **min(list)** - finds the minimum value in a list
- **max(list)** - finds the maximum value in a list
- **mean(list)** - finds mean value of list
- **sum(list)** - adds all values together
- average
   - can use sum(list) divided by len(list) to find the total sum and divide it by the total number of items
- **abs(value)** - returns the absolute value of a specified number

# Dictionaries

- a collection of unordered, modifiable (mutable) paired (key: value) data type

# Creating a dictionary

- can create a dictionary two ways:
   - using curly brackets {}
   - dict() built in function
- dictionaries can be created empty
- values could be any data type
- keys should be string or ints
- can access dictionary items using the key name and square brackets

## Modifying dictionaries

- can check the number of key value pairs in a dictionary using **len(dict)**
- if you try to access an item by a key name that doesn’t exist it will error out
   - to avoid this check if the key exists using the **get()** method
      - `dict.get(‘key’)`
   - can also use the in operator to check if a key exists
- Can add new key and value pairs to a dictionary by specifying key and value
   - dct[‘key’] = ‘value’
   - if key doesn’t exist it will create new key value pair
   - if key does exist this will modify value
- **Pop(key)** - removes the item with the specified key name
- **popitem()** - removes the last item
- **del** keyword - removes an item with a specified key name or deletes the dictionary entirely
- **items()** - changes a dictionary into a list of tuples (immutable)
- **clear()** - empties a dictionary
- **copy()** - can copy a dictionary without modifying the original
- **keys()** - outputs all keys as a list
- **values()** - outputs all values as a list

