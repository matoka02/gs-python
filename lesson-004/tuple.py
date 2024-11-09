a = (1, 2, 3, 4, 5, 5, 4)
print(a[0], a[1], a[2])
print(a[:2], a[-2:])

# a[0] = 8        # TypeError: 'tuple' object does not support item assignment

print('-------------------------')

print(a.count(5), a.count(4))
print(a.index(4))