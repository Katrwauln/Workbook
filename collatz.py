def collatz(number):
   
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

try:
    number = input('Give me a number: ')
    while number != 1:
        number = collatz(int(number))
except ValueError:
    print('Value Error. Please enter an integer.')


