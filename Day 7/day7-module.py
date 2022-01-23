# write a function which generates random six digit id
import random
import string
def random_user_id():
    random_id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(6)])
    return random_id

print(random_user_id())

# modify function to take two inputs
def user_id_gen_by_user():
    num_char = input("How many characters should the id be?: ")
    num_id = input("How many IDs are supposed to be generated?: ")
    id = 1
    id_lst = []
    while id <= int(num_id):
        random_id = ''.join([random.choice(string.ascii_letters
                + string.digits) for n in range(int(num_char))])
        id_lst.append(random_id)
        id += 1
    return id_lst
print(user_id_gen_by_user())

# write a function that generates rgb colors - 3 values ranging from 0 to 255
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = [r,g,b]
    return "rgb({},{},{})".format(r,g,b)

print(rgb_color_gen())
    
# return any number of hexadecimals in an array
def list_hexa(num_colors):
    num = 1
    arr_hexa = []
    while num <= num_colors:
        hexadecimal = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
        arr_hexa.append(hexadecimal)
        num += 1
    return arr_hexa

print(list_hexa(3))

# return any number of RGB colors in an array
def list_of_rgb_colors(num_colors):
    num = 0
    arr_rgb = []
    while num < num_colors:
        rgb = rgb_color_gen()
        arr_rgb.append(rgb)
        num += 1
    return(arr_rgb)

print(list_of_rgb_colors(3))

# generate any number of hexa or rgb colors
def generate_colors(type, num_colors):
    num = 0
    list = []
    if type == 'hexa':
        return list_hexa(num_colors)
    elif type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Type not acceptable"
        
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))
        

# takes a list and returns a shuffled list
def shuffled_list(lst):
    random.shuffle(lst)
    return lst

mylist = ["apple", "banana", "cherry"]
print(shuffled_list(mylist))

# returns an array of seven random numbers in 0-9 range and all numbers must be unique
def unique_arr(num):
    items = random.sample(range(0,9), num)
    return items

print(unique_arr(7))