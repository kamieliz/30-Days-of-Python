# find most frequent word in a paragraph
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def most_frequent_words(string):
    from collections import Counter
    # returns list of all words in string
    split_str = string.split()

    # pass to instance of counter
    Counter = Counter(split_str)

    most_freq = Counter.most_common(4)
    return most_freq

print(most_frequent_words(paragraph))

# write a pattern which identifies valid python variables
def is_valid_variable(s):
    import re
    return bool(re.search(r'', s))

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))

# clean text then find most frequent words
def clean_text(sentence):
    import re
    cleaned_text = re.sub('$|%|@|#|;|&', '', sentence)
    return cleaned_text
    
    
filled_sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean = clean_text(filled_sentence)
print(clean)
print(most_frequent_words(clean))