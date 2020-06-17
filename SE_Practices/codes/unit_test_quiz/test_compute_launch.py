from SE_Practices.codes.unit_test_quiz.compute_launch import days_until_launch

def test_days_until_launch_4():
    assert (days_until_launch(22, 26) == 4)


def test_days_until_launch_0():
    assert (days_until_launch(253, 253) == 0)


def test_days_until_launch_0_negative():
    assert (days_until_launch(83, 64) == 0)


def test_days_until_launch_1():
    assert (days_until_launch(9, 10) == 1)


def test_days_pelin_5():
    assert (days_until_launch(10, 15) == 5)


def test_days_pelin_0_negative():
    assert (days_until_launch(15, 10) == 0)


# python -m pytest /Users/pelin.balci/PycharmProjects/aws_ml_foundations/SE_Practices/codes/unit_test_quiz/test_compute_launch.py

'''
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/pelin.balci/PycharmProjects/aws_ml_foundations
collected 6 items                                                                                                                                         

SE_Practices/codes/unit_test_quiz/test_compute_launch.py ......                                                                                     [100%]

==================================================================== 6 passed in 0.03s ==

'''