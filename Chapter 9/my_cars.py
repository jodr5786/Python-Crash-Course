from car import Car
from electric_car import ElectricCar

my_truck = Car('gmc', 'canyon', 2018)
print(my_truck.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model x', 2019)
print(my_tesla.get_descriptive_name())