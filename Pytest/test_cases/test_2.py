import pytest

"""
Pytest Fixture:
    Fixtures are used when we need to run a code before every test. To do so we need to create a code that we want to 
    run before test and decorate it with the @pytest.fixture. Now, when ever we need to run that code before tests we
    have to pass the fixture function name as a variable to that test.
    
    We can only use the fixture inside this file, if we want to use the fixture in multiple files we have to write the 
    fixture in conftest.py file. The pytest library will first look for the fixture inside the file if it can't find 
    the fixture it will look in the conftest file located in the project folder.
"""


@pytest.fixture
def assign_values():    # fixture inside the file
    a = 5
    b = 6
    c = 7
    return [a, b, c]


def test_case2_1(assign_values):
    assert assign_values[0] == 6, 'assign_values[0] is not equal to 6.'


def test_case2_2(assign_values1):       # fixture inside the conftest file.
    assert assign_values1[0] == 7, 'assign_values1[0] is not equal to 6.'


def test_case2_3(assign_values):
    assert assign_values[0] > 6, 'assign_values[0] is less than 6.'
