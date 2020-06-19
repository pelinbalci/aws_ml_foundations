from OOP.codes.modular_shirt_class import Shirt

shirt_one = Shirt('yellow', 'M', 15)
print(shirt_one.get_price())

shirt_one.set_price(10)
print(shirt_one.get_price())