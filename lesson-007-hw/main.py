class Vehicle:
    def __init__(self, model, make, year, vehicle_type):
        self.model = model
        self.make = make
        self.year = year
        self.vehicle_type = vehicle_type

    def model_type(self):
        print(f'Model: {self.model}')
        print(f'Make by: {self.make}')
        print(f'Year: {self.year}')
        print(f'Type of Vehicle: {self.vehicle_type}')

    def full_type_check(self):
        pass

    def display_info(self):
        print(
            f"It's a {self.vehicle_type}, Make by: {self.make}, Model type: {self.model}, Year of manufacture: {self.year}")


class Car(Vehicle):
    def __init__(self, model, make, year, fuel_type, vehicle_type):
        super().__init__(model, make, year, vehicle_type)
        self.fuel_type = fuel_type

    def full_type_check(self):
        if self.fuel_type == 'Patrol' or self.fuel_type == 'Gas':
            print(f'You broke your {self.vehicle_type}')
        else:
            print('Fuel type accepted')

    def start_engine(self):
        if self.fuel_type != 'Patrol' and self.fuel_type != 'Gas':
            print('Engine started')
        else:
            print('Engine cannot be started')

    def display_info_1(self):
        print(f'Fuel type: {self.fuel_type}')


class Motorcycle(Vehicle):
    def __init__(self, model, make, year, fuel_type, vehicle_type):
        super().__init__(model, make, year, vehicle_type)
        self.fuel_type = fuel_type

    def full_type_check(self):
        if self.fuel_type == 'Diesel' or self.fuel_type == 'Gas':
            print(f'You broke your {self.vehicle_type}')
        else:
            print('Fuel type accepted')

    def start_engine(self):
        if self.fuel_type != 'Diesel' and self.fuel_type != 'Gas':
            print('Engine started')
        else:
            print('Engine cannot be started')

    def display_info_2(self):
        print(f'Fuel type: {self.fuel_type}')


class Bicycle(Vehicle):
    def __init__(self, model, make, year, vehicle_type, type_of_road):
        super().__init__(model, make, year, vehicle_type)
        self.type_of_road = type_of_road

    def move(self):
        print(f'{self.vehicle_type} is moving.')

    def display_info_3(self):
        print(f'Type of road: {self.type_of_road}')


car = Car('Toyota', 'Corolla', 2020, 'Petrol', 'Car')
motorcycle = Motorcycle('CBR500', 'Honda', 2019, 'Diesel', 'Motorcycle')
bicycle = Bicycle('Giant', 'Defy Advanced Pro 0', 2021, 'Bicycle', 'Asphalt')

car.full_type_check()
car.start_engine()
car.model_type()
print('---------------------------')

motorcycle.full_type_check()
motorcycle.start_engine()
motorcycle.model_type()
print('--------------------------')

bicycle.move()
bicycle.model_type()
print('---------------------------')

car.display_info()
motorcycle.display_info()
bicycle.display_info()