o_file = open('split.txt')
r_file = o_file.read()

fword = r_file.find('forumes')
emaile = r_file.find(' ',fword)
emailw = r_file[fword:emaile]

print(emailw)
