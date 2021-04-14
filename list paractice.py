my_list = ['zaabi', 'me', 'sultan']

for x in my_list :
    print(x)
print('i just finished')

for l in my_list:
    print('how are you',l+'?')

print(my_list[1])

my_list[1] = 30
print(my_list[1])
print(my_list)


a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)
print(10 not in c)

print(sum(c) / len(c))

numlist = list()

while True :
    usernum = input('enter a number ')
    if usernum == 'done' : break
    value = float(usernum)
    numlist.append(value)
    print(numlist)
    print(sum(numlist*len(numlist)))


