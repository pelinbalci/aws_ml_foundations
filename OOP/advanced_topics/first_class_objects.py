# Ref: https://realpython.com/primer-on-python-decorators/

# In Python, functions are first-class objects.
# This means that functions can be passed around and used as arguments

# Example
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(say_hello))  # Hello Bob
print(greet_bob(be_awesome)) # Yo Bob, together we are the awesomest!


# Another Example
import math


def exp_value(x):
    return math.sqrt(x)


def take_square(x):
    return x**2


def do_something(func1, func2):
    x = func1(5)
    return func2(x)


print(do_something(exp_value, take_square))
print(do_something(take_square, exp_value))
