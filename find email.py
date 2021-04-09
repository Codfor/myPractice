ofile = open('1.txt')

line = ofile.read()

emailStart = line.find('forumes')
print(emailStart)
emailEnd = line.find(' ',emailStart)-2 # added -2 to remove 'we' from the second line which comes before the space
print(emailEnd)
fullEmail = line[emailStart:emailEnd]
print(fullEmail)


