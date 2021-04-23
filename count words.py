my_file = open('count words.txt')
read_file = my_file.read()

# to read all text in the file line by line
# for w in my_file :
#     print(w)

# to read all text in the file line by line while taking the new line out at the end of each line
# for w in my_file :
#     print(w.rstrip())

# # find a word 'tickets' from the file
# first_word = read_file.find('tickets')
# last_word = read_file.find('/',334) # to find '/' after the word 'tickets
# print(first_word)
# print(last_word)
# full_word = read_file[first_word:last_word] # to split word 'ticket' from entire text file
# print(full_word)


# create a list without spaces from the text file
# the_list = list()
# split_words = read_file.split() # to split the text file into word by word
#
# for w in split_words:
#     if w == ' ':
#         continue
#     the_list.append(w) # add the word if its not blank space to the list
# print(the_list)

# ##create a list without spaces from the text file
# the_list = list()
# split_words = read_file.split() # to split the text file into word by word
# for w in split_words:
#     if w == ' ':
#         continue
#     the_list.append(w) # add the word if its not blank space to the list
# print(the_list.count('to')) # cont how many time word 'to' in the file


the_list = list()
split_words = read_file.split() # to split the text file into word by word
dic_list =dict()
print(split_words)

# for w in split_words:
#     if w not in dic_list: # if the word is not in the dictionary the added it
#         dic_list[w] = 1
#     else: # otherwise add 1 to it to count how many times it wad mentioned in the file
#         dic_list[w]= dic_list[w]+1
# print(dic_list)

for w in split_words:
    dic_list[w] = dic_list.get(w, 0) + 1 # count how many time the words mentioned. similar to above example but with less words
# print(dic_list)

# for x in dic_list:
#     print(x,dic_list[x]) # print the key (x) and the value

print(list(dic_list)) # print a list without values from the dictionary

print(dic_list.values()) # print only the values of the dictionary


print(dic_list.items()) # create tuple from a dictionary
