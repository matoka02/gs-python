num_1 = 100
num_2 = 10

num_3 = num_1 + num_2
print(num_3)

num_3 = num_1 - num_2
print(num_3)

num_3 = num_1 * num_2
print(num_3)

num_3 = num_1 / num_2
print(num_3)

num_4 = 7
num_5 = 2

num_6 = num_4 / num_5
num_7 = num_4 // num_5
print(num_6, num_7)

num_8 = 5
num_9 = 2

num_10 = num_8 ** num_9
print(num_10)

num_11 = num_4 % num_5
print(num_11)

num_12 = 10
num_13 = 5

num_14 = num_12 == num_13
print(num_14)       # false

num_14 = num_12 != num_13
print(num_14)       # true

num_14 = num_12 < num_13
print(num_14)       # false

num_14 = num_12 > num_13
print(num_14)       # true

print('****')

num = 10
name = "Tom"

result = num > 5 and name == "Tom"
print(result)       # true

result = num < 5 or name == "Tom"
print(result)       # true

result = num < 5 and name == "Tom"
print(result)       # false

print('****')

message = "Tom get some money"
print(name in message)
print(name not in message)

name = "John"
message = "You won!"
print(name in message)
print(name not in message)

age = 50
name = "Irina"
animal = "Cat"

print(age == 50 and "Ira" in name and animal != "dog")      # true
print(age == 50 and "I" in name or animal == "dog")         # true
print(age == 50 and "F" in name and animal != "dog")        # false