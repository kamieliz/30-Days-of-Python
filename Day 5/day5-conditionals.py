# if condition
a = 3
if a > 0:
    print('A is a positive number')
    
# if else
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
    
# if elif else
a = 0
if a < 0:
    print('A is a negative number')
elif a > 0:
    print('A is a positive number')
else:
    print('A is zero')

# if statements all in one line
a = 3
print('A is positive') if a > 0 else print('A is negative')

# nested conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# if with and operator
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative') 

# if with or operator
user = 'James'
access_level = 4
if user ==  'admin' or access_level >= 4:
    print('Access Granted!')
else:
    print('Access Denied!')

# Exercises
# get user input if user is 18 or older and give feedback
age = input("Enter your age: ")
age = int(age)
missing_years = 0
if age >= 18:
    print("You are old enough to know how to drive")
else:
    missing_years = 18 - age
    print("You need {} more years to learn to drive".format(missing_years))

# compare the values of my age and your age
my_age = 27
your_age = input("Enter your age: ")
your_age = int(your_age)
difference = 0
if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print("You are {} years older than me.".format(difference))
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("You are 1 year younger than me.")
    else:
        print("You are {} years younger than me.".format(difference))
else:
    print("We are the same age!")

# get two numbers from input and check which is greater, less or equal
a = input("Choose a number: ")
a = int(a)
b = input("Choose a second number: ")
b = int(b)
if a > b:
    print("{} is greater than {}".format(a,b))
elif a < b:
    print("{} is less than {}".format(a,b))
else:
    print("{} is equal to {}".format(a,b))

# grade students based on scores
grade = input("What was your grade on the test: ")
grade = int(grade)
if grade <= 100 and grade >= 90:
    print("You got an A!")
elif grade < 90 and grade >= 80:
    print("You got an B!")
elif grade < 80 and grade >= 70:
    print("You got an C.")
elif grade < 70 and grade >= 60:
    print("You got an D.")
elif grade > 100 or grade < 0:
    print("Please try again with a score between 0-100")
else:
    print("You got an F.")

# check what season it is
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
month = input("What month is it?: ")
if month in autumn:
    print("The season is autumn")
elif month in winter:
    print("The season is winter")
elif month in spring:
    print("The season is spring")
elif month in summer:
    print("The season is summer")
else:
    print("Try again and make sure to capitalize first letter of the month")

# add new fruit if not already in list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("What is your favorite fruit?: ")
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exists in the list')

# check if person has skills key, print middle skill
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
middle = int(len(person["skills"]) / 2)
if "skills" in person:
    middle_skill = person["skills"][middle]
    print("This person's middle skill is {}".format(middle_skill))

# check if person has python in skills list
if "skills" in person:
    if "Python" in person["skills"]:
        print("This person has Python in their skills")

# check what kind of developer they are based on listed skills
if "MongoDB" in person["skills"] and "Node" in person["skills"]:
    if "React" in person["skills"]:
        print("This person is a full stack developer")
    elif "Python" in person["Skills"]:
        print("This person is a backend developer")
elif "Javascript" in person["skills"]:
    print("This person is a frontend developer")
else:
    print("This person's title is unknown")

# check if they are married and where they live
if person["is_married"]:
    country = person["country"]
    name = person["first_name"]
    print("{} lives in {}. He is married".format(name, country))

