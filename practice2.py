ofile = input('whats the file name? ')

# if the user enters a wrong file name it will show a message then quit the app
try:
    oofile = open(ofile)
except:
    print('file not available')
    quit() # to stop the program from continue

# print line that starts with text hello
for txt in oofile :
    if txt.startswith('hello') :
        print(txt)