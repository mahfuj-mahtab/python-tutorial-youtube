while True:
    num1 = float(input('Enter 1st number : '))
    operator = input('Enter symbol like [+,-,*,/] :')
    num2 = float(input('Enter 2nd number : '))

    if(operator == '+'):
        print(num1, operator,num2, '=', num1 + num2)
    elif(operator == '-'):
        print(num1, operator,num2, '=', num1 - num2)
    elif(operator == '*'):
        print(num1, operator,num2, '=', num1 * num2)
    elif(operator == '/'):
        print(num1, operator,num2, '=', num1 / num2)
    else:
        print('Wrong operation!')

