# Day 5 - Conditionals & Control Flow

# Table of Contents

1. [Conditionals](craftdocs://open?blockId=39BFD28A-949C-4D5A-8250-D018DC165FEB&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [If condition](craftdocs://open?blockId=42B79147-2AB3-4038-9FDF-82A00A293710&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [If Else](craftdocs://open?blockId=E610A310-D357-4818-A3C7-8209B23E5B08&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   3. [If Elif Else](craftdocs://open?blockId=6B9B3BB1-53DA-4550-82EF-2C80CB943893&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   4. [Short hand](craftdocs://open?blockId=8B4A666E-450C-43CC-9B83-23B6F0014C20&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   5. [Nested Conditions](craftdocs://open?blockId=1EC1167C-EE0F-4029-99DF-E4538625A0D3&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   6. [If and logical operators](craftdocs://open?blockId=56DB93A5-9229-4247-BB2B-8AE4F9767E6E&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   7. [If or logical operator](craftdocs://open?blockId=3EBB32A1-A4EB-4F64-B1D9-90EC75197288&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# Conditionals

- by default, statements in python are executed sequentially from top to bottom
- if the processing logic requires it, the sequential flow of execution can be altered in two ways:
   - conditional execution: a block of one or more statements that will execute if a certain expression is true
   - repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true

## If condition

- In python, the key word if is used to check if a condition is true and to execute the block code
- remember the indentation after the colon
- if the condition is false we do not see a result

```other
if condition:
		this part of code runs if true
```

## If Else

- in order to see a result from a false condition, we need to add another block called else.
- if the condition isnt true, the else condition will run

```other
if condition:
		this part runs if true
else:
		this part runs if false
```

## If Elif Else

- sometimes we make decisions by checking multiple conditions
- elif keyword allows you to add multiple conditions to your if statement

```other
if condition:
		code
elif condition:
		code
else:
		code
```

## Short hand

- if statements can be written all in one line as a form of shorthand

```other
code if condition else code
```

## Nested Conditions

- conditions can be nested together similar to loops
- this is not recommended and can be avoided using logical operators

```other
if condition:
		code
		if condition:
				code
```

## If and logical operators

- two combine two conditions use the and operator
- both conditions must be true for the statement within to run

```other
if condition and condition:
		code
```

## If or logical operator

- combines two conditions together
- only one condition needs to be true for the statement to run

```other
if condition or condition
		code
```

