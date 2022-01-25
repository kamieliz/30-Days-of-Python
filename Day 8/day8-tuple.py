# create an empty tuple
empty = ()

# join two tuples
sisters = ('Kadiyah','Yasmine','Lateefah')
brothers = ('Elijah', 'Saludeen')
siblings = sisters + brothers
print(siblings)
print(len(siblings))

# add another tuple to joined tuple
parents = ('Elizabeth', 'Roosevelt')
family_members = parents + siblings
print(family_members)

# unpack siblings and parents from family_members
parent_slice = family_members[0:2]
sibling_slice = family_members[2:]
print(parent_slice)
print(sibling_slice)

# create three tuples and join them
fruits = ('banana', 'orange', 'apple')
veggies = ('broccoli', 'carrots', 'peas')
meat = ('pork', 'beef', 'chicken')
food_stuff_tp = fruits + veggies + meat
print(food_stuff_tp)

# change tuple to list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(type(food_stuff_lt))

# slice out middle item
print(len(food_stuff_tp))
middle = int(len(food_stuff_tp) / 2)
middle_item = food_stuff_tp[middle]
print(middle_item)

# slice out first 3 and last 3 items
first_three = food_stuff_tp[:3]
print(first_three)
last_three = food_stuff_tp[-4:]
print(last_three)

# delete tuple
del food_stuff_tp

# check if item exists
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Iceland' in nordic_countries:
    print('Iceland is a Nordic country.')