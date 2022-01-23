# Day 6 - String Formatting

# Table of Contents

1. [String Formatting](craftdocs://open?blockId=64C8FF93-3F1D-49D9-9548-547167C29A90&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Old Style String Formatting (% Operator)](craftdocs://open?blockId=D0B36340-C658-4C45-A143-36026D4E8050&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [New Style String Formatting (str.format)](craftdocs://open?blockId=7020704F-1D23-4F0E-8CD3-9FA9811C98F6&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   3. [String Interpolation/f- strings](craftdocs://open?blockId=90A42A15-D50F-4755-A6DF-5EC2753456D6&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# String Formatting

## Old Style String Formatting (% Operator)

- In python there are many ways of formatting strings
- the “%” operator is used to format a set of variables enclosed in a “tuple” (a fixed size list), together with a format string, contains normal text with argument specifiers
   - %s - string or any object with a string representation lik numbers
   - %d - integers
   - %f - floating point numbers
   - %.number of digitsf - floating point numbers with fixed precision

`formatted_string = "I am %s %s. I teach %s" %(str1,str2,str3)`

## New Style String Formatting (str.format)

- this formatting is introduced in python version 3
- format() method takes arguments to fill in {} in string

`formatted_string = “I am {} {}. I teach {}”.format(str1, str2, str3)`

## String Interpolation/f- strings

- Strings start with f and we can inject the data in their corresponding positions

`print(f’{a} + {b} = { a+b }’)`

# Python Strings as Sequences of Characters

- python strings are sequences of characters and share their basic methods of access with other Python ordered sequences of objects like lists and tuples
- simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables
   - `a,b,c,d,e,f = string-var`
- the first letter of a string is at zero index and the last letter of a string is the length of a string minus one
   - can start from right end using negative indexing. -1 is the last index
   - `string[-1]`
- Can slice strings into substrings
   - `string[1:3]`
- can reverse strings
   - `string[::-1]`
- possible to skip characters while slicing by passing step argument to slice methods
   - `str[0:6:2]`

# String Methods

- capitalize() - converts the first character of the string to capital letter
   - `str.capitalize()`
- count() - returns occurrences of substring in string, count(substring, start=, end=)
   - the start is a starting indexing for counting
   - end is the last index to count
   - `str.count(substring, start=,end=)`
- endswith() - checks if a string ends with a specified ending
   - `str.endswith(‘substring’)`
- expandtabs() - replaces tab character with spaces
   - default tab size is 8
   - it takes tab size argument
   - `str.expandtabs(tabsize)`
- find() - returns the index of the first occurrence of a substring, if not found returns -1
   - `str.find(‘substring’)`
- rfind() - returns the index of the last occurrence of a substring, if not found returns -1
   - `str.rfind(‘substring’)`
- format() - formats string into a nicer output
   - `str.format(str(), str())`
- index() - returns the lowest index of a substring, additional arguments indicate starting and ending index
   - default - 0
   - string length default - 1
   - if substring is not found, it raises a valueError
   - `str.index(‘substring’, num)`
- rindex() - returns the highest index of a substring, additional arguments indicate starting and ending index
   - `str.rindex(‘substring’, num)`
- isalnum() - checks alphanumberic character
   - returns boolean, True or False
   - `str.isalnum()`
- isalpha() - checks if all string elements are alphabet characters (a-z and A-Z)
   - `str.isalpha()`
   - returns boolean
- isdecimal() - checks if all characters in a string are decimal (0-9)
   - `str.isdecimal()`
   - returns boolean
- isdigit() - checks if all characters in a string are numbers
   - `str.isdigit()`
   - returns boolean
- isnumeric() - checks if all characters in a string are numbers or number related, accepts more symbols than isdigit()
   - `str.isnumer()`
   - returns boolean
- isidentifier() - checks for a valid identifier
   - checks if a string is a valid variable name
   - `str.isidentifier()`
   - returns boolean
- islower() - checks if all alphabet characters are lowercase
   - `str.islower()`
   - returns boolean
- isupper() - checks if all alphabet characters are uppercase
   - `str.isupper()`
   - returns boolean
- join() - adds strings to together
   - returns the concatenated string
   - `str.join(‘list of strings’)`
- strip() - removes all given characters starting from the beginning and end of the string
   - `str.strip(‘substring’)`
- replace() - replaces substring with a given string
   - `str.replace(‘substring’, ‘replacement’)`
- split() - splits the string, using given string or space as a separator
   - `str.split(‘separator’)`
- title() - returns a title cased string
   - `str.title()`
- swapcase() - converts all uppercase characters to lowercase and lowercase to uppercase
   - `str.swapcase()`
- startswith() - checks if string starts with specified string
   - `str.startswith(‘substring’)`

