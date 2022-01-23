# formatting with % operator
# strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formatted_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formatted_string)

# strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formatted_string)

# new style string formatting
formatted_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formatted_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))

# string interpolation
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')

# unpacking characters
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# access by index
language = 'Python'
first_letter = language[0]
print(first_letter)
last_letter = language[-1]
print(last_letter)

# slicing strings
first_three = language[0:3]
print(first_three)
last_three = language[-3:]
print(last_three)

# reversing a string
greeting = 'Hello, World!'
print(greeting[::-1])

# skipping characters while slicing
language = 'Python'
pto = language[0:6:2] # use step argument
print(pto)
