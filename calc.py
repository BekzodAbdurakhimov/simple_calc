try:
    number_one = int(input('Enther the first number: '))
except ValueError:
    print('The first input is not a number')
    exit()

math_symbol = input('Enther the arithmetic sign (+, -, *, /): ')
if math_symbol not in ('+', '-', '*', '/'):
    print('Wrong arithmetic symbol!')
    exit()

try:
    number_two = int(input('Enter the second number: '))
except ValueError:
    print('The second input is not a number')
    exit()

if math_symbol == '+':
    result = number_one + number_two
elif math_symbol == '-':
    result = number_one - number_two
elif math_symbol == '*':
    result = number_one * number_two
elif math_symbol == '/':
    if number_two == 0:
        print('Zero Division Error')
        exit()
    result = number_one / number_two
else:
    print('The arithmetic symbol is incorrect')
    exit()

print(f'The result of {number_one} {math_symbol} {number_two} = {result}')
