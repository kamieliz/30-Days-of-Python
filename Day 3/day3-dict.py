# create a dictionary with curly brackets
empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

# dictionary values can be any data type
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250, #int
    'country':'Finland',
    'is_marred':True, #boolean
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], #list
    'address':{ #dictionary
        'street':'Space street', 
        'zipcode':'02210'
    }
    }

# check length
print(len(dct))

# access items using key name
print(dct['key1'])
print(person['first_name'])

# if key name doesn't exist, it will raise an error
# print(dct['key4'])
# prevent this by checking if key exists first
print(dct.get('key4')) # if doesn't exist will print none
print('key4' in dct) # should be false if doesnt exist

# add new item
dct['key4'] = 'value4'
print(dct)

# modify an item
person['age'] = 249
print(person)

# remove an item with pop()
dct.pop('key1')
print(dct)

# remove last item with popitem()
dct.popitem()
print(dct)

# remove with del
del dct['key2']
print(dct)

# clear a dictionary
dct.clear()
print(len(dct))

# delete a dictionary
del dct

# copy a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
dct_copy = dct.copy()
print(dct_copy)

# get all keys in a dictionary
print(person.keys())

# get all values in a dictionary
print(person.values())



