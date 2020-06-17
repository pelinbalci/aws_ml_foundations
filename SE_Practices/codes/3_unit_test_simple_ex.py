###################
# test a function #
###################


def nearest_square(num):
    """
    :param num: integer
    :return: the nearest square that is less than or equal to sum
    """
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2


###################
# my way:) --> it is not repeatable and automated :(
###################
num = 12
output = nearest_square(num)
print('output of ' + str(num) + ' is: ', output)
print(output < num)

###################
# second way --> write expected results manually. We need to check the output manually. :(
###################

print('expected output of ' + str(5) + ' is: 4, output is: ', nearest_square(5))
print('nearest square <= 5:  returned {}, correct answer is 4.'.format(nearest_square(5)))

###################
# use assert --> it checks the expected results automatically
###################

num_5 = nearest_square(5)
print('nearest square <= 5:  returned {}, correct answer is 4.'.format(num_5))
assert(num_5 == 4)  # if correct it doesn't give an output.


num_5 = nearest_square(5)
print('nearest square <= 5:  returned {}, correct answer is 3.'.format(num_5))
assert(num_5 == 3)  # wrong! the result is messy :(

#Traceback (most recent call last):
#  File "/Users/pelin.balci/PycharmProjects/aws_ml_foundations/SE_Practices/codes/3_unit_test_simple_ex.py", line 43, in <module>
#    assert(num_5 == 3)
# AssertionError

# Since we get an error above, rest of the script broke.
num_12 = nearest_square(12)
print('nearest square <= 5:  returned {}, correct answer is 9.'.format(num_12))
assert(num_12 == 9)  # we could't see the solution :(