countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# use map to create a new list where each country is uppercase
def change_to_upper(name):
    return name.upper()
countries_upper = list(map(change_to_upper, countries))
print(countries_upper)

# use map to create a new list where the numbers are squared
def square(x):
    return x ** 2
numbers_squared = list(map(square, numbers))
print(numbers_squared)

# use filter to filter out countries containing land
def contains_land(name):
    if 'land' in name:
        return True
    return False
land_names = list(filter(contains_land, countries))
print(land_names)


# use filter to filter out countries having exactly 6 characters
def exactly_six_char(name):
    if len(name) == 6:
        return True
    return False
countries_six_char = list(filter(exactly_six_char, countries))
print(countries_six_char)

# use reduce to sum all numbers
from functools import reduce
def sum_all(x,y):
    return x + y
total = reduce(sum_all, numbers)
print(total)

# use reduce to concatenate all countries and produce a sentence
# desired output =  Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
first_half = reduce(lambda a,b: a + ', ' + b, countries)
final_str = first_half + " are north European countries"
print(final_str)

