def nearest_square(num):
    """
    :param num: integer
    :return: the nearest square that is less than or equal to sum
    """
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2


def test_nearest_square_5():
    assert(nearest_square(5) == 4)


def test_nearest_square_12():
    assert(nearest_square(12) == 9)


# pytest /Users/pelin.balci/PycharmProjects/aws_ml_foundations/SE_Practices/codes/test_nearest.py

'''
===================================================================== test session starts =====================================================================
platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/pelin.balci/PycharmProjects/aws_ml_foundations
collected 2 items                                                                                                                                             

SE_Practices/codes/test_nearest.py ..                                                                                                                   [100%]

====================================================================== 2 passed in 0.01s ===
'''