# Ref: https://realpython.com/primer-on-python-decorators/
# Whenever you call parent(), the inner functions first_child() and second_child() are also called.


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()
# Printing from the parent() function
# Printing from the second_child() function
# Printing from the first_child() function

# We can't call second_chil() or first_child() directly.


def new_parent(order):
    print("I am parent")

    def new_first_child():
        print("I am the first child")

    def new_second_child():
        print("I am the second child")

    if order == 1:

        return new_first_child()
    else:
        return new_second_child()

new_parent(1)
# I am parent
# I am the first child

my_first_child = new_parent(1)
# I am parent
# I am the first child

my_second_child = new_parent(2)
# I am parent
# I am the second child
