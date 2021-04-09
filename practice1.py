ofile = open('1.txt')

#print line by line
for txt in ofile :
    print(txt.rstrip())  # rstrip added to take extra space or new line at the end of each line
print('finish')

