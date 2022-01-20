# while loop
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count) # this will be executed once count = 5
# while loop with break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break  # loop only prints 0,1,2


# while loop with continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # only skips 3
    print(count)
   

# for loop with list
numbers = [0,1,2,3,4,5]
for number in numbers: # number is a temp name to refer to list items, only valid inside loop
    print(number) # numbers will be printed line by line
    
# for loop with string
language = 'Python'
for letter in language:
    print(letter)
    
# for loop with tuple
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

# for loop with dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# for loop with set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
    
# for loop with break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# for loop with continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# testing range function
lst = list(range(11))
print(lst) 

st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst)

# for loop with range()
for number in range(11):
    print(number)

# nested for loop
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# exercises

# iterate 0 to 10 using a for loop
for number in range(10):
    print(number)

# iterate 0 to 10 using a while loop
count = 0
while count < 11:
    print(count)
    count = count + 1

# iterate 10 to 0 using a while loop
while count > 0:
    print(count)
    count = count - 1

# write a nested loop to make a triangle
for i in range(0,5):
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")

# use loop to print pattern
for i in range(11):
    product = i * i
    print("{0} x {0} = {1}".format(i, product))
    
# iterate through a list with for loop
languages = ['Python', 'Numpy', 'Pandas', 'Django','Flask']

for l in languages:
    print(l)

# iterate through 100 and print only even
for i in range(0,100,2):
    print(i)

# use for loop to iterate through 0 to 100 and print sum of all numbers
sum = 0
for i in range(0,101):
    sum += i
print("The sum of all numbers is {}".format(sum))

# use for loop to iterate through 0 to 10 and print sum of evens 
# and print sum of odds
e_sum = 0
o_sum = 0
for i in range(0,101):
    if i % 2:
        o_sum += i
    else:
        e_sum += i
print("The sum of all evens is {}. And the sum of all odds is {}".format(e_sum, o_sum))

# reverse list with while loop
fruits = ['banana', 'orange', 'mango', 'lemon']
i = len(fruits) - 1
while i >= 0:
    print(fruits[i])
    i -= 1
