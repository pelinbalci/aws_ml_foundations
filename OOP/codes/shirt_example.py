
# Ref: https://github.com/udacity/DSND_Term2/blob/master/lessons/ObjectOrientedProgramming/JupyterNotebooks/1.OOP_syntax_shirt_practice/shirt_exercise.ipynb

# Capitalize the first letter in class name. () or not.
# self stores your attributes; colors, size etc. --> makes those attributes available throught your class.
# self is a dictionary that holds your attributes and attributes values.
# if you want to access these attributes: self will be the first input to the functions.
# change price doesn't return anything. It only changes the value of price attribute.
# discount method returns discounted price.
# you can't reach object name ; for example shirt_1.
# you can change the attributes directly: shirt_1.color = 'black' Try not to use this way.
# Read more: https://www.python-course.eu/python3_properties.php


class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


# create object
new_shirt = Shirt('yellow', 'S', 'short', 15)
# <__main__.Shirt object at 0x1068ee8d0>
# new shirt has now color,  price, size and style attributes and values.
print(new_shirt.price)
print(new_shirt.color)

# Use methods:
new_shirt.change_price(10)  # this method change the value of the price.
print(new_shirt.price)

discounted_price = new_shirt.discount(0.2)  # this method produce a new variable using discount param.
print(discounted_price)


# Store the objects in a list:
shirt_list = []
shirt_1 = Shirt('red', 'S', 'short', 15)
shirt_2 = Shirt('yellow', 'M', 'long', 12)
shirt_3 = Shirt('blue', 'S', 'V-necked', 18)

shirt_list.extend((shirt_1, shirt_2, shirt_3))

new_prices_list = []
discount_ratio = 0.2
for i in range(len(shirt_list)):
    shirt = shirt_list[i]
    new_prices = shirt_list[i].discount(discount_ratio)
    new_prices_list.append(new_prices)
print(new_prices_list)

####################
# QUIZ #
####################

shirt_one = Shirt('red', 'S', 'long-sleeve', 25)
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

# use methods:
shirt_one.change_price(10)
print('new price of shirt_one:', shirt_one.price)

new_price_one = shirt_one.discount(0.12)
print('disocunted price for one:', new_price_one)

# Calculate total revenue
total = shirt_one.price + shirt_two.price
print('total_cost:', total)

# Calculate total discount
total_discount = shirt_one.discount(0.14) + shirt_two.discount(0.06)
print('total discount:', total_discount)


# Unit tests to check your solution
from OOP.codes.test_shirt_ex import run_tests
run_tests(shirt_one, shirt_two, total, total_discount)