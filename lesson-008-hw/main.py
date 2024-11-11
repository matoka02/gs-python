from abc import ABC, abstractmethod

# task 1

class User:
    def __init__(self):
        self.__name = ''
        self.__email = ''
        self.__password = ''

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password


user = User()
user.set_name('Alian Ford')
user.set_email('alian201935@gmail.com')
user.set_password('Alian-3523')
print('User name: ', user.get_name())
print('E-mail: ', user.get_email())
print('Password: ', user.get_password())
print('------------------------------')

# task 2

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(9, 3)
triangle = Triangle(6, 2)
print('Area of circle: ', circle.calculate_area())
print('Area of the rectangle: ', rectangle.calculate_area())
print('Area of the triangle: ', triangle.calculate_area())
