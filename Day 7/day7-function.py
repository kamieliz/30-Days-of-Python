# declare a function that takes 2 parameters and returns a sum
def add_two_numbers(a, b):
    return a + b
    
print(add_two_numbers(3,5))

# write function that calculates area of circle
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return(area)

print(area_of_circle(10))

# write function that adds sum of all arguments and takes arbitrary args
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add_all_nums(3,5,7,9))

# convert celsius to fahrenheit
def convert_celsius_to_fahrenheit(temp):
    new_temp = (temp * (9/5)) + 32
    return new_temp
    
print(convert_celsius_to_fahrenheit(20))

# check what season a month is in
def check_season(month):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']
    if month in autumn:
        season = "The season is autumn"
    elif month in winter:
        season = "The season is winter"
    elif month in spring:
        season = "The season is spring"
    elif month in summer:
        season = "The season is summer"
    else:
        season = ("Try again and make sure to capitalize first letter of the month")
    return season
    
print(check_season("December"))

# take a list as a parameter and print out each element
def print_list(lst):
    for item in lst:
        print(item)

autumn = ['September', 'October', 'November']
print(print_list(autumn))

# take an array and return the reverse
def reverse_list(arr):
    new_list = arr[::-1]
    return new_list

print(reverse_list(autumn))

# takes a list and returns a capitalized list of items
def capitalize_list_items(lst):
    lst = [item.capitalize() for item in lst]
    return lst
    
fruits = ['banana', 'orange', 'mango', 'lemon']
print(capitalize_list_items(fruits))

# returns a list with an item added at the end
def add_item(lst, item):
    lst.append(item)
    return lst

print(add_item(fruits, 'apple'))

# remove an item from a list
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(fruits, 'apple'))

# take a number and add all the numbers in that range
def sum_of_range(number):
    sum = 0
    for num in range(0, number + 1, 1):
        sum = sum + num
    return sum
print(sum_of_range(5))

# takes a number and adds only the odd numbers
def sum_of_odds(max):
    odd_total = 0
    for number in range(0, max + 1):
        if number % 2 != 0:
            odd_total = odd_total + number
    return odd_total
        
print(sum_of_odds(7))

# takes positive integer and count number of evens and odds
def evens_and_odds(pos_int):
    e_total = 0
    o_total = 0
    final = []
    for num in range(0, pos_int + 1):
        if num % 2 == 0:
            e_total += 1
        elif num % 2 != 0:
            o_total += 1
    final.extend((e_total, o_total))
    return final

print(evens_and_odds(100))

# checks if something is empty
def is_empty(var):
    if bool(var):
        val = "This variable isn't empty"
    else:
        val = "This variable is empty"
    return val

a_variable = {}
print(is_empty(a_variable))

# check if all items are unique in a list
def all_unique(lst):
    s = set()
    for item in lst:
        if item in s: return False
        s.add(item)
    return True
print(all_unique(fruits))

# checks if all items are the same data type
def same_type(lst):
    res = True
    for ele in lst:
        if not isinstance(ele, type(lst[0])):
            res = False 
            break
    return res

print(same_type(fruits))

# write a function to check for a valid python variable
def valid_var(str):
    return str.isidentifier()

print(valid_var("Hello_world"))