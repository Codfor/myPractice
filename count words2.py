# count most used word in a text file

word_counter = dict()

# enter the text you want to count words
open_file = input('enter your text: ')

# split words to create a list for the dictionary
read_file = open_file.split()
print(read_file)

# loop through the list to add words and their counts to the dictionary
for words in read_file :
    word_counter[words]= word_counter.get(words, 0)+1
print(word_counter)

# print the key and the value using old method
# for values in word_counter:
#     print(values, word_counter[values])

# print the key and value using new method
# for a, b in word_counter.items(): # items create tuple from the dictionary
#     print(a, b)

# loop through the dictonary to find the most used words based from its count

most_word = None
most_count = None
for key, value in word_counter.items():
    if  most_count is None or value > most_count:
        most_word=key
        most_count=value
print('the most used word is',most_word,'by', most_count)