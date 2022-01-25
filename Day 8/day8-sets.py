# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# find length of it_companies
it_length = len(it_companies)
print(it_length)

# add Twitter to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert Multiple IT companies at once
it_companies.update(['F5', 'VMware', 'Hashicorp'])
print(it_companies)

# remove one company
it_companies.remove('F5')
print(it_companies)

# join A and B
joined_set = a.union(b)
print(joined_set)

# find A intersection B
intersection_set = a.intersection(b)
print(intersection_set)

# is A subset of B
if a.issubset(b):
    print("A is subset of B")
else:
    print('A is not subset of B')

# are A and B disjoint sets
if a.isdisjoint(b):
    print('A and B are disjoint sets')
else:
    print('A and B are joint sets')
    
# difference A and B
difference_set = a.difference(b)
print(difference_set)

# symmetric difference A and B
sym_diff_set = a.symmetric_difference(b)
print(sym_diff_set)

# delete sets
del a
del b

# convert ages to a set compare length
age_set = set(age)
print(age_set)
if len(age_set) > len(age):
    print('Age as a set is longer than Age as a list')
elif len(age_set) < len(age):
    print('Age as a set is shorter than Age as a list')
else:
    print('Age is the same length as a set and as a list') 

# convert sentence to set to get unique words
sent_list = "I am a teacher and I love to inspire and teach people".split()
sent_set = set(sent_list)
print(sent_set)
print(len(sent_set))
