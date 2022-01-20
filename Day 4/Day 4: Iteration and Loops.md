# Day 4: Iteration and Loops

# Table of Contents

1. [Loops](craftdocs://open?blockId=D6EF15ED-598C-4E32-9C05-78827C8812B8&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [While loops](craftdocs://open?blockId=5711B559-D813-43A1-B7CF-6E54DB4F311A&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [For Loops](craftdocs://open?blockId=95B3CF4F-981E-4EFE-9966-EAD57E013417&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# Loops

- in order to handle repetitive task programming languages loops are used
- In python there are two types of loops:
   - while
   - for

## While loops

- **while** is a reserved word for making while loops
- used to execute a block of statements repeatedly until a given condition is satisfied
- When the condition becomes false, the lines of code after the loop will be executed

```other
while condition:
		code goes here
```

- **break** is a key word we can use to get out of or stop the loop

```other
while condition:
		code goes here
		if another_condition:
				break
```

- **continue** is used to skip the current iteration and continue with the next

```other
while condition:
		code goes here
		if another_condition:
				continue
```

## For Loops

- for keyword is used to make a for loop, similar to for loops in other programming languages but with some differences in syntax
- For loops are used for iterating over a sequence
   - lists
   - tuples
   - dictionaries
   - sets
   - strings
- if youre looping through a list

```other
for iterator in list:
		code goes here
```

- If you’re looping a string

```other
for iterator in string:
		code goes here
```

- when you loop through a dictionary, it outputs the keys of the dictionary

```other
for key in dict:
	code

# to print keys and values
for key, value in dict.items():
	print(key,value)
```

- Break can be used in a loop to stop it before its complete

```other
for iterator in sequence:
		code goes here
		if condition:
				break
```

- Continue can be used to skip some of the steps in the iteration of the loop

```other
for iterator in sequence:
		code goes here
		if condition:
				continue
```

- the range() function prints a list of numbers
   - takes three parameters: starting, ending, increment
   - default it starts from 0 and the increment is 1
   - the range sequence needs at least 1 argument (end)

```other
for iterator in range(start, end, step):
		code goes here
```

- you can write loops inside of a loop, this is called a nested loop

```other
for x in y:
		for t in x:
				print(t)
```

- if you want to execute something after the loop ends use else

```other
for iterator in range(start,end,step):
	do something
else:
	print('The loop ended')
```

- Pass is a keyword you can use to avoid errors when a statement requires code but we don't want to execute anything there
   - this is also used as a placeholder for future statements

```other
for iterator in sequence:
		pass
```

