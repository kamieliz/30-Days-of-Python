# Day 12 - Error Types and Datetime objects

# Table of Contents

1. [Error Types](craftdocs://open?blockId=ECF25E0C-C056-4CDA-AA46-6696AF91674E&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [SyntaxError](craftdocs://open?blockId=D7BB35E5-5A8A-423E-BBCF-5D86C780B23C&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [NameError](craftdocs://open?blockId=A29DBF7E-FBCC-470B-8F14-1C5BA6E1D24D&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   3. [Index Error](craftdocs://open?blockId=E6C5531C-D830-4964-B162-8B15B07156A2&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   4. [ModuleNotFoundError](craftdocs://open?blockId=7240030D-01D3-48D9-AE44-19F337E40E6B&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   5. [AttributeError](craftdocs://open?blockId=CFF1CEC1-3909-49CD-B700-50A4C0D6E4A1&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   6. [KeyError](craftdocs://open?blockId=29350BDF-8C62-43A3-B03A-1F1C086BB19F&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   7. [TypeError](craftdocs://open?blockId=BFCFD5A9-C351-478C-8797-8B78B3D568C1&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   8. [ImportError](craftdocs://open?blockId=2CC18345-B7DD-4233-96BC-8FD8973C56D1&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   9. [ValueError](craftdocs://open?blockId=0C206AD3-557F-4E75-8434-D53F5A267042&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   10. [ZeroDivisionError](craftdocs://open?blockId=3FEBE9C2-B3BD-45A9-91C3-92C399FB6387&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# Error Types

- if code fails to run, the python interpreter will display a message, containing feedback with information on where the problem occurs and the type of error
- sometimes the interpreter will give suggestions on a possible fix
- understanding different error types will help debug your code quickly and improve your programming

## SyntaxError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

## NameError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

## Index Error

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

## ModuleNotFoundError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

## AttributeError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

## KeyError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

## TypeError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

## ImportError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

## ValueError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

## ZeroDivisionError

```other
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

# DateTime Objects

- the datetime module is used to handle dates and times
- with dir or help built in commands its possible to know the available functions in a certain module
- can perform mathematical functions on this type of object

```other
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

## Datetime function

- import the datetime function from the datetime module
- datetime.now() creates an object with different attributes you can view
   - day
   - month
   - year
   - hour
   - minute
   - second
   - timestamp - number of seconds elapsed from 1st of january 1970 UTC
- to create a datetime object use datetime()
   - `new_year = datetime(2020,1,1)`

## Formate Date Output using strfttime

- you can format datetime objects using the strftime method
- can convert strings to datetime objects using this method
   - `date_object = datetime.strptime(date_string, "%d %B, %Y”)`
- strfttime symbols are used to format time

![Image](https://res.craft.do/user/full/d367a179-adcb-7ce8-0b02-ba52d2a7c917/doc/6C423EFE-3411-4254-BACA-9760AAD84BF4/68CD7267-A609-4F27-842B-B4676DD77970_2/Image)

## Date function

- just focuses on the year, month, and day of a datetime object
- import this function from datetime module
- can use today() to get a date object for todays date

```other
from datetime import date
d = date(2020, 1, 1)
print('Current date:', d.today())    # 2019-12-05
```

## Time function

- represents time objects, just hour, minute and second
- import this from datetime module

```other
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
```

## Timedelta function

- used to find the difference between two points in time
- import from datetime module

```other
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

