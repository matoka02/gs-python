# 1 task
example_string = 'tessa'
example_int = 35
example_float = 35.4
example_bool = False
example_list = ['hello', 'my', 'nickname', 'is', example_string]
example_tpl = (example_string, example_float)
example_dct = {'nickname': example_string, 'age': example_float}
example_var = None
# print(example_dct)


# 2 task
result = example_string == 'tessa' and example_int == 35
result2 = example_string == 'tessa' and example_bool == False
print(result2)
print(example_float == 35.4 and 'S' in example_string)


# 3.1 task
num_str=125
print(type(num_str))
num_str = str(num_str)
print(type(num_str))

# 3.2 task
message = 'Hi, my name is Python!'
new_message = message.replace('y', '0').replace('i', '1')
print(new_message)

# 3.3 task
split_test = 'This is a split test'
split_test=split_test.split()
split_join=' '.join(split_test)
print(split_join)

# 3.4 task
print(len(split_join))


# 4.1 task
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

# 4.2 task
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

# 4.3 task
print(list_extend.index(6))

# 4.4 task
print(len(list_append))


# 5.1 task
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'], dict_test['where'])

# 5.2 task
print(dict_test.keys())
print(dict_test.values())

# 5.3 task
print(dict_test.items())