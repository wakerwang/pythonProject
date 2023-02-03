# coding:utf-8

from car import Car, ElectricCar

my_beetle=Car('volkswagen','beetle',2020)
print(my_beetle.get_descriptive_name())


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
