"""
Monkeypatching/Mocking test:

"""
import test_3_api

""" lambda: value 
        This line is used to create a function which returns the value.
    For example:
    def func1():
        return  1
    
    If you want to change the return value of func1 to 10, you can use the below code but we can change it simply by
    using the lambda as shown below.
    
    def func1():
        return 10
    
    The above function can be replaced with 
    
    func1 = lambda: 10"""

import unittest
from unittest.mock import patch
from test_3_api import len_joke


def func1():
    return 1


# print(func1())

func1 = lambda: 10


# print(func1())


class TestJoke(unittest.TestCase):  # This is a test class to test the len_joke func in test_3_api module using mock.

    """ This will patch the get_joke function, which means the return value of this function will be replaced with the
        given value in the test function. In this case, the return value parameter is mock_get_joke."""

    @patch('test_3_api.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'      # Assigning the mock_get_joke return value to one.
        self.assertEqual(len_joke(), 3, 'Not equal to length of joke')      # Testing the case using assertEqual method.

    @patch('test_3_api.get_joke')
    def test_original_len_joke(self, joke):
        joke.return_value = test_3_api.get_joke()
        print(joke)
        length_joke = len(joke)
        self.assertEqual(length_joke, len(joke), 'length is not equal')
