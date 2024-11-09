import utilities

# task 2

def main():
    numbers = [10, 34, 65, 78, 100]
    average = utilities.calculate_average(numbers)
    print('Average value: ', average)
    max_number = utilities.find_max(numbers)
    print('Max value: ', max_number)

if __name__ == '__main__':
    main()