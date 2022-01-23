# concatenate list of strings to a single string
list_str = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(list_str)
print(result)

# declare variable and print length
company = 'Coding For All'
print(company)
print(len(company))

# change all characters to uppercase
print(company.upper())

# change all chacters to lowercase
print(company.lower())

# format string with capitalize
print(company.capitalize())

# format with title
print(company.title())

# format with swapcase
print(company.swapcase())

# slice first word out of string
first_word = company[0:6]
print(first_word)

# check if string contains word
if company.find('Coding') >= 0:
    print("String contains Coding")
    
# replace coding with python
print(company.replace('Coding', 'Python'))

# change string to Python for Everyone
print(company.replace('Coding', 'Python').replace('All', 'Everyone'))

# split string using space as separator
print(company.split())

# split bigger string at the comma
it_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(it_companies.split(', '))

# what character is at index 0
first_letter = company[0]
print(first_letter)

# what is last index of string
last_letter = company[-1]
print(last_letter)

# what character is at index 10
index_ten = company[10]
print(index_ten)

c_for_a = 'Coding For All'
p_for_e = 'Python For Everyone'

# use index to determine first occurrence of C
c_index = c_for_a.index('C')
print(c_index)

# use index to determine first occurrence of F
f_index = c_for_a.index('F')
print(f_index)

# use find to determine last occurrence of l
last_l = c_for_a.rfind('l')
print(last_l)

# find first occurrence of because
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_bc = sentence.find('because')
print(first_bc)

# find last occurence of because
last_bc = sentence.rindex('because')
print(last_bc)

# print because slice
slice_bc = sentence[first_bc: ]
print(slice_bc)

# start with Coding
if c_for_a.startswith('Coding'):
    print("The sentence does start with Coding")

# end with Coding
if c_for_a.endswith('coding'):
    print("The sentence ends with coding.")
else:
    print("The sentence does not end with coding")

# see which variable name is valid
var_nm_1 = '30DaysOfPython'
var_nm_2 = 'thirty_days_of_python'

if var_nm_1.isidentifier():
    print("30DaysOfPython is a valid variable name")
elif var_nm_2.isidentifier():
    print("thirty_days_of_python is a valid variable name")
else:
    print("Neither string is a valid variable name")

# join list with hash and space
libraries = ['Django','Flask','Bottle','Pyramid','Falcon']
print('# '.join(libraries))

# separate two sentences using \n
print("I am enjoying this challenge.\nI just wonder what is next")
# use tab escape sequence to print
print("Name\tAge\tCountry\tCity")
print('Asabeneh\t250\tFinland\tHelsinki')

# display lines with string formatting
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))

# math with string formatting
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a,b, a // b))
print('{} ** {} = {}'.format(a,b, a**b))
