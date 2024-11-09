import calculator

# task 1

def choose_operation():
    print('Select operation:')
    print('1. Adding (+)')
    print('2. Subtraction (-)')
    print('3. Multiplication (*)')
    print('4. Division (/)')
    choice = input('Enter the operation number: ')
    return choice

def main():
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    operation = choose_operation()

    if operation == '1':
        print('Result:', calculator.add(a, b))
    elif operation == '2':
        print('Result:', calculator.subtract(a, b))
    elif operation == '3':
        print('Result:', calculator.multiply(a, b))
    elif operation == '4':
        print('Result:', calculator.divide(a, b))
    else:
        print('Error')

if __name__ == '__main__':
    main()

