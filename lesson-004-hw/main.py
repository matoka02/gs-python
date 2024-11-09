## lists

# task 1
a = [1, 2, 3, 4, 5]
print(a)
a.append(10)
a.append(20)
a.remove(10)
print(a)
print('-------------------------')

# task 2
a = [1, 2, 3, 4, 5]
total_sum = sum(a)
print(total_sum)
print('-------------------------')

# task 3
a = [1, 2, 3, 4, 5]
b = [number *2 for number in a]
print(b)
print('-------------------------')

## tuples

# task 1
fruits = ('apple', 'banana', 'orange')
for fruit in fruits:
    print('Element: ', fruit)
print('-------------------------')

# task 2
a = ('apple', 'banana', 'orange')
b = (1, 2, 3)
c = b + a
print(c)
print('-------------------------')

## dictionaries

# task 1
list = {'name': 'Jon', 'age': 21, 'country': 'USA', 'sport': 'football'}
for key, value in list.items():
    print(f"{key}: {value}")
print('-------------------------')

# task 2
books = {
    'Master and Margarita': 1967,
    'The little prince': 1943,
    "Harry Potter and the Philosopher's Stone": 1997,
}
copy_books = books.copy()
dict_update = {"Harry Potter and the Chamber of Secrets": 1998}
books.update(dict_update)
print(books)
print('-------------------------')

# task 3
countries_capitals = {
    'Ukraine': 'Kyiv',
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Slovakia': 'Bratislava',
}

country = input('Enter the name of the country: ')
capital = countries_capitals.get(country)

if capital:
    print(f'Capital of the country {country}: {capital}')
else:
    print(f'The country {country} is not in the database.')
print('-------------------------')
