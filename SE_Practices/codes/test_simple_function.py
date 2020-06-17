import SE_Practices.codes.simple_function as sf

# correct
def test_nearest_square_5():
    assert(sf.nearest_square(5) == 4)

# false
def test_nearest_square_12():
    assert(sf.nearest_square(12) == 5)

# correct
def test_nearest_square_20():
    assert(sf.nearest_square(20) == 16)


# false
def test_nearest_square_30():
    assert(sf.nearest_square(30) == 23)


# from SE_Practices.codes import simple_function also working.
# Don't write pytest /Users/pelin.balci/PycharmProjects/aws_ml_foundations/SE_Practices/codes/test_simple_function.py
# --> NOT WORKING

# Write terminal:
# (https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada/34140498#34140498)
# python -m pytest /Users/pelin.balci/PycharmProjects/aws_ml_foundations/SE_Practices/codes/test_simple_function.py



########################
# correct
########################

'''
===================================================================== test session starts ==============================
platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/pelin.balci/PycharmProjects/aws_ml_foundations
collected 2 items                                                                                                                                             

SE_Practices/codes/test_simple_function.py ..        [100%]

====================================================================== 2 passed in 0.02s ===
'''

########################
# Fails:
########################

'''
===================================================================== test session starts ==============================
platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/pelin.balci/PycharmProjects/aws_ml_foundations
collected 2 items                                                                                                                                             

SE_Practices/codes/test_simple_function.py .F  [100%]

========================================================================== FAILURES ====================================
___________________________________________________________________ test_nearest_square_12 _____________________________

    def test_nearest_square_12():
>       assert(sf.nearest_square(12) == 5)
E       assert 9 == 5
E        +  where 9 = <function nearest_square at 0x104a97680>(12)
E        +    where <function nearest_square at 0x104a97680> = sf.nearest_square

SE_Practices/codes/test_simple_function.py:9: AssertionError
=================================================================== short test summary info ============================
FAILED SE_Practices/codes/test_simple_function.py::test_nearest_square_12 - assert 9 == 5
================================================================= 1 failed, 1 passed in 0.17s =====

'''

########################
# After the middle one fails:
########################

'''
===================================================================== test session starts ==============================
platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/pelin.balci/PycharmProjects/aws_ml_foundations
collected 3 items                                                                                                                                             

SE_Practices/codes/test_simple_function.py .F.                                    [100%]

========================================================================== FAILURES ====================================
___________________________________________________________________ test_nearest_square_12 _____________________________

    def test_nearest_square_12():
>       assert(sf.nearest_square(12) == 5)
E       assert 9 == 5
E        +  where 9 = <function nearest_square at 0x107ee8b90>(12)
E        +    where <function nearest_square at 0x107ee8b90> = sf.nearest_square

SE_Practices/codes/test_simple_function.py:9: AssertionError
=================================================================== short test summary info ============================
FAILED SE_Practices/codes/test_simple_function.py::test_nearest_square_12 - assert 9 == 5
================================================================= 1 failed, 2 passed in 0.17s =

'''

########################
# two fails two passes:
########################

'''

===================================================================== test session starts =====================================================================
platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/pelin.balci/PycharmProjects/aws_ml_foundations
collected 4 items                                                                                                                                             

SE_Practices/codes/test_simple_function.py .F.F                                                                                                         [100%]

========================================================================== FAILURES ===========================================================================
___________________________________________________________________ test_nearest_square_12 ____________________________________________________________________

    def test_nearest_square_12():
>       assert(sf.nearest_square(12) == 5)
E       assert 9 == 5
E        +  where 9 = <function nearest_square at 0x1021ca050>(12)
E        +    where <function nearest_square at 0x1021ca050> = sf.nearest_square

SE_Practices/codes/test_simple_function.py:9: AssertionError
___________________________________________________________________ test_nearest_square_30 ____________________________________________________________________

    def test_nearest_square_30():
>       assert(sf.nearest_square(30) == 23)
E       assert 25 == 23
E        +  where 25 = <function nearest_square at 0x1021ca050>(30)
E        +    where <function nearest_square at 0x1021ca050> = sf.nearest_square

SE_Practices/codes/test_simple_function.py:18: AssertionError
=================================================================== short test summary info ===================================================================
FAILED SE_Practices/codes/test_simple_function.py::test_nearest_square_12 - assert 9 == 5
FAILED SE_Practices/codes/test_simple_function.py::test_nearest_square_30 - assert 25 == 23
================================================================= 2 failed, 2 passed in 0.14s ==

'''