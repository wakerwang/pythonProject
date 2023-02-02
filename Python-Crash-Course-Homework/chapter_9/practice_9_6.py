# coding:utf-8


class Restaurant:
    # 创建一个饭馆的类
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.restaurant_name + " is open. Come on in!"
        print("\n" + msg)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand("The Big One")
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.open_restaurant()
