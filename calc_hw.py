def calculator():
    try:
        first_number = int(input('Enter the first number: '))
    except ValueError:
        print('The first input is NOT a number')
        return

    symbol = input('Enther the arithmetic sign (+, -, *, /): ')
    if symbol not in ('+', '-', '*', '/'):
        print('Wrong arithmetic symbol!')
        return

    try:
        second_number = int(input('Enther the second number: '))
    except ValueError:
        print('The second input is NOT a number')
        return

    if symbol == '+':
        result = first_number + second_number
    elif symbol == '-':
        result = first_number - second_number
    elif symbol == '*':
        result = first_number * second_number
    elif symbol == '/':
        if second_number == 0:
            print('Zero Division Error')
            return
        result = first_number / second_number
    else:
        print('The arithmetic sign is incorrect')
        return

    print(f'The result of {first_number} {symbol} {second_number} = {result}')

calculator()