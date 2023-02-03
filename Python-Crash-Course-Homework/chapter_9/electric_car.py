# coding:utf-8

from car import Car

class Battery:
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 60:
            range = 140
        else:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"Upgraded the battery to {self.battery_size} kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
