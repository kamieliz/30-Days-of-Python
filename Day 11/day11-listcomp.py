# filter only negative and zero in the list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero = [n for n in numbers if n <= 0]
print(neg_zero) # [ -4 , -3, -2, -1, 0]

# flatten list of lists of lists to one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = lambda irregular_list:[element for item in irregular_list for element in flat_list(item)] if type(irregular_list) is list else [irregular_list]
print(flat_list(list_of_lists))

# create a list of tuples
lst_tup = [(i, 1, i * 1, i * i, i * i * i, i * i * i * i, i * i * i * i * i) for i in range(11)]
print(lst_tup)

