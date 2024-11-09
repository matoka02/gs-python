a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']

print(a[0], a[1], a[-1])
print(b[1])

print(a[1:4], a[::2], a[::])
print(b[::2])

print(a[::-1])
print(b[::-1])

print('-------------------------')

a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']

a.append(6)
b.append('tomato')
print(a, b)

a.insert(3, True)
b.insert(3, 'bottle')
print(a, b)

a.remove(True)
b.remove('bottle')
print(a, b)

print('-------------------------')

a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']

last_elem_a = a.pop()
last_elem_b = b.pop()
print(last_elem_a, last_elem_b)

first_elem_a = a.pop(0)
first_elem_b = b.pop(0)
print(a.index(3), b.index('banana'))

a.extend([5, 5, 5])
b.extend(['cherry', 'banana', 'banana'])
print('5: ', a.count(5), '; banana: ', b.count('banana'), '; cherry: ', b.count('cherry'))

print('-------------------------')

a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']

print(a, b)
a.sort(reverse=True)
b.sort()
print(a, b)
a.reverse()
b.reverse()
print(a, b)