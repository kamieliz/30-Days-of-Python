# Day 14 - Regular Expressions

# Regular Expressions

- A regular expression is a special text string that helps to find patterns in data
- They can be used to check if some pattern exists in a different datat type
- to use regex in python you must first import the RegEx module called re
   - `import re`

## Methods in re module

- to find a pattern we use different set of re character sets that allows to search for a match in a string

### Match

- searches only in the beginning of the first line of string and returns matched objects if found, else returns None
- only returns an object only if the text starts with the pattern

```other
# syntax
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
```

### Search

- returns a match object if there is one anywhere in the string, including multiline strings
- looks for the pattern throughout the text but returns only the first match that was found

```other
# syntax
re.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag
```

### findAll

- better than search because it checks for the pattern through the whole string and returns all the matches as a list
- the re.I flag checks for both lowercase and uppercase matches

```other
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

### Sub

- replacing a substring if it matches the pattern

```other
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
```

### Split

- splitting text into separate strings

```other
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol
```

## Writing RegEx Patterns

- to declare RegEx variable r'
- []: A set of characters
   - [a-c] means, a or b or c
   - [a-z] means, any letter from a to z
   - [A-Z] means, any character from A to Z
   - [0-3] means, 0 or 1 or 2 or 3
   - [0-9] means any number from 0 to 9
   - [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
- \ : uses to escape special characters
   - d means: match where the string contains digits (numbers from 0-9)
   - D means: match where the string does not contain digits
- . : any character except new line character( )
- ^: starts with
   - r'^substring' eg r'^love', a sentence that starts with a word love
   - r'[^abc] means not a, not b, not c.
- $: ends with
   - r'substring$$' eg r'love$$', sentence that ends with a word love
- *: zero or more times
   - r'[a]*' means a optional or it can occur many times.
- \+: one or more times
   - r'[a]+' means at least once (or more)
- ?: zero or one time
   - r'[a]?' means zero times or once
- {3}: Exactly 3 characters
- {3,}: At least 3 characters
- {3,8}: 3 to 8 characters
- |: Either or
   - r'apple|banana' means either apple or a banana
- (): Capture and group

![Image](https://res.craft.do/user/full/d367a179-adcb-7ce8-0b02-ba52d2a7c917/doc/2EBB8E1A-FE77-4486-AB24-3AEBD092E4CF/404A28F7-1414-43DE-892C-B0187AE941C9_2/Image)

