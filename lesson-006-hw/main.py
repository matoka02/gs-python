# task 1

class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f'{self.name}, {self.sound}')


animal_1 = Animal('Murka', 'Cat', 7, 'purr')
animal_2 = Animal('Archie', 'German Shepherd', 5, 'barks')

animal_1.make_sound()
animal_2.make_sound()

print('------------------------------')

# task 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        if self.width < 0 or self.height < 0:
            print('Error: The sides of a rectangle cannot be negative.')
        else:
            area = self.height * self.width
            print(f'Area of the rectangle: {area}')


Rectangle_1 = Rectangle(1, 67)
# Rectangle_2 = Rectangle(-34, 1000)
Rectangle_3 = Rectangle(65, 80)

# Rectangle_2.calculate_area()
Rectangle_1.calculate_area()
Rectangle_3.calculate_area()