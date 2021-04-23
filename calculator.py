
def add (num1, num2):
    return num1 + num2

def sub (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

selection = int(input('select desired calculation\n1. add\n2. sub\n3. multiply\n4.divide\n enter your selection: '))

f_number = int(input('what is your first number? '))
s_number = int(input('what is your second number? '))

if selection == 1:
    print(f_number , '+' , s_number , '=', f_number+s_number)
elif selection == 2 :
    print(f_number , '-' , s_number , '=', sub(f_number,s_number))
elif selection == 3 :
    print(f_number , '+' , s_number , '=' , multiply(f_number,s_number))
elif selection == 4 :
    print(f_number, '/', s_number, '=', divide(f_number,s_number))
