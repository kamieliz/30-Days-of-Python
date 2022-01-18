# creating a list with built in function
lst = list() # creates empty list
print(len(lst)) # length should equal 0 since its empty

# creating a list with square brackets
nlst = [] # creates empty list

# find the length of a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(len(fruits)) # prints length

# lists can contain items of different ypes
diff_list = ['Hey', 250, True, {'country':'Finland', 'city':'Helsinki'}]
print(diff_list)

# can access list items with index
first_fruit = fruits[0]
print(first_fruit)

# negative indexing allows accessing from the end
last_fruit = fruits[-1]
print(last_fruit)

# unpacking list items
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark','Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# list slicing
all_fruits = fruits[0:] # grabs every index
orange_mango = fruits[1:3] # does not include the first index
orange_mango_lemon = fruits[1:] # all items excluding first index
orange_and_lemon = fruits[::2] # this uses the step argument every other item
print(all_fruits)
print(orange_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

# negative index - list slicing
all_fruits = fruits[-4]
print(all_fruits)
orange_and_mango = fruits[-3:-1] # start with 2 from start end with last
print(orange_and_mango)
reverse_fruits = fruits[::-1] # negative step takes list in reverse order
print(reverse_fruits)

# modifying list section
it_companies = ['Facebook', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(it_companies))
# print last company
print(it_companies[-1]) 
# print first company
print(it_companies[0])
# print middle company  
middle = int(len(it_companies) / 2)
print(it_companies[middle]) 
# add a company to list
it_companies.append('F5')  
print(it_companies)
# insert a company to middle of list
it_companies.insert(middle, 'VMware') 
print(it_companies)
# make on name uppercase
it_companies[0] = it_companies[0].upper() 
print(it_companies)
# join list together with #; in between
print("#; ".join(it_companies)) 
# check if microsoft is in list
print('Microsoft' in it_companies) 
# sort list
it_companies.sort() 
print(it_companies)
# reverse list
it_companies.reverse()
print(it_companies)
# slices out first 3 companies
print(it_companies[:3]) 
# slices out last 3 companies
print(it_companies[-3:]) 
# slice out middle companies
print(it_companies[1:-2])
# remove first company
it_companies.remove('VMware')
print(it_companies)
# remove middle commpany
it_companies.remove('IBM')
print(it_companies)
# remove last company
it_companies.remove('Amazon')
print(it_companies)
# destroy list
it_companies.clear()
print(len(it_companies))
# Join two lists and assign it to a variable
new_list = fruits + countries
print(new_list)

