# Ref: https://realpython.com/primer-on-python-decorators/

#############
# Decorator #
##############


def my_decorator(func):
    def my_inner_function():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return my_inner_function


def say_hello():
    print("Hello!")


speak = my_decorator(say_hello)
speak()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


#############
# Decorator with @ #
##############

#  use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax.
def my_decorator(func):
    def wrapper():
        print("Pie syntax: sth is happening before the function is called.")
        func()
        print("Pie syntax: sth is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")


say_whee()
# Output:
# Pie syntax: sth is happening before the function is called.
# Whee!
# Pie syntax: sth is happening after the function is called.


####################
# REuse the decorators #
####################

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_hello():
    print('hellooo!!')

say_hello()
# hellooo!!
# hellooo!!


#############
# With Arguments #
#############

# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
# greet("Pelin")
# Returns error: wrapper_do_twice() takes 0 positional arguments but 1 was given


# In order to solve this error define do_twice function with arguments:
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Pelin")
# Hello Pelin
# Hello Pelin

#############
# Return values #
#############


def do_twice_new(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)  # it returns another print function + hi {name}, that's why we see it three times.
    return wrapper_do_twice


@do_twice_new
def greeting(name):
    print("Return values")
    return f"Hi {name}"


print(greeting("Pelin"))
# Output:
# Return values
# Return values
# Return values
# Hi Pelin


