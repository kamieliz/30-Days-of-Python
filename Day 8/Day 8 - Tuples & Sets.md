# Day 8 - Tuples & Sets

# Table of Contents

1. [Tuples](craftdocs://open?blockId=0F8806A9-EDAB-46B9-88F8-A4C60F071DAF&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Tuple Methods](craftdocs://open?blockId=C04D9992-B33A-48F9-A5A3-4EAB0B6B1C14&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [Creating a Tuple](craftdocs://open?blockId=B2F33606-4835-43B4-9F5F-DADB59B0A217&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   3. [Working with Tuples](craftdocs://open?blockId=C63EFBD7-E85B-4EC5-93BE-D85A5C65F68B&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# Tuples

- collection of different data types which is ordered and unchangeable
- written with round brackets ()
- once created, values cannot change
- cannot use add, insert, remove methods in a tuple

## Tuple Methods

- tuple(): to create an empty tuple
- count(): to count the number of a specified item in a tuple
- index(): to find the index of a specified item in a tuple
- \+: can join two or more tuples together to create a new one

## Creating a Tuple

- Empty tuple

```other
empty_tuble = ()
# or use the tuple constructor
empty_tuple = tuple()
```

- tuple with initial values

```other
# syntax
tpl = ('item1', 'item2','item3')
```

- use len() to get length of a tuple

```other
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

## Working with Tuples

- can use positive indexing to access tuple items

```other
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```

- can also use negative indexing

```other
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```

- slice tuples into sub-tuple

```other
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
```

- change tuples to lists and vice versa

```other
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

- check whether an item exists in a tuple

```other
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

- join two or more with + operator

```other
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

- its not possible to remove an item but is possible to delete the tuple

```other
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

# Sets

- collection of unordered and un-indexed distinct elements
- used to store unique items
- possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets

## Creating a set

- can use curly brackets or set() built-in function to create a set

```other
# syntax
st = {}
# or
st = set()
```

- creating a set with initial items

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

- use len() method to fight length

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(set)
```

## Accessing Items in a Set

- check if an item exist in a list use in operator

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

- add an item to the set, can not change any existing items

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

- add multiple items using update(). takes a list argument

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

- can remove itels using remove() if item not found, raises errors. can also use discard() to remove without erroring out

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

- pop() method removes a random item from a list and returns it

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

- to clear or empty the set

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

- to delete the set itself

```other
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

- convert list to set and vice versa

```other
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

   - converting list to set removes duplicates and only unique items will be reserved
- can join two sets using the union() and that returns a new set

```other
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

- can join two sets using update() inserts a set into another set

```other
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

- Intersection returns a set of items which are in both the sets

```other
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```

- a set can be a subset or super set of other sets:
   - subset: issubset()
   - superset: issuperset()

```other
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

- difference() returns the difference between two sets

```other
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

- symmetric_difference() reurns a set that contains all items from both sets except items that are present in both sets

```other
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```

- if two sets do not have a common item or items they are disjoint sets. Can check with isdisjoint()

```other
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

