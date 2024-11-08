## Conditional constructions

# task 1
password = 'password123'
user_password = input('Enter password: ')
if user_password == password:
    print('You are logged in')
else:
    print('Wrong password')
print('-------------------------')

# task 2
day_number = int(input('Enter the day of the week number (1-7): '))
if day_number == 1:
    print('Monday')
elif day_number == 2:
    print('Tuesday')
elif day_number == 3:
    print('Wednesday')
elif day_number == 4:
    print('Thursday')
elif day_number == 5:
    print('Friday')
elif day_number == 6:
    print('Saturday')
elif day_number == 7:
    print('Sunday')
else:
    print('Invalid day number')
print('-------------------------')

## Loops

# task 1
number = int(input('Enter number (1-10): '))
print('Multiplication table for', number)

for a in range(1, 11):
    print(number, '*', a, '=', number * a)
print('-------------------------')

# task 2
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_numbers = 0
for d in list_of_numbers:
    sum_of_numbers += d
print('Sum of numbers: ', sum_of_numbers)
print('-------------------------')

# task 3
b = 9
factorial = 1
for a in range(1, b + 1):
    factorial *= a
print('The factorial of a number', b, 'is equal to', factorial)
print('-------------------------')

# task 4
for number in range(1, 51):
    if number % 2 == 0:
        print(number)
print('-------------------------')

# task 5
a = 10
b = 30
print('Prime numbers in the range from', a, 'to', b, ':')
for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
print('-------------------------')