# calc_project

number_one = int(input('Enter the first number: '))
# operation = input('Enter the arithmetic sign: ')
# number_two = int(input('Enter the second number: '))

if type(number_one) is int:
    operation = input('Enter the arithmetic sign: ')
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('Wrong arithmetic symbol!')
    else:
        number_two = int(input('Enter the second number: '))
        if type(number_two) is int:
            if operation == '+':
                print(f'{number_one} + {number_two} = {number_one + number_two}')
            elif operation == '-':
                print(f'{number_one} - {number_two} = {abs(number_one - number_two)}')
            elif operation == '*':
                print(f'{number_one} * {number_two} = {number_one * number_two}')
            elif operation == '/':
                if number_one <= 0 < number_two < 0 <= number_one:
                    print('Zero division error')
                else:
                    print(f'{number_one} / {number_two} = {abs(number_one / number_two)}')
            else:
                print('The arithmetic symbol is incorrect')
        else:
            print(f'{number_two} is not a number')
else:
    print(f'{number_one} is not a number')