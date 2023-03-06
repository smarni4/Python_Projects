"""
Monkeypatching/Mocking test:

"""
import test_3_api
import requests

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

# func1 = lambda: 10


# print(func1())


class TestJoke(unittest.TestCase):  # This is a test class to test the len_joke func in test_3_api module using mock.

    """ This will patch the get_joke function, which means the return value of this function will be replaced with the
        given value in the test function. In this case, the return value parameter is mock_get_joke."""

    @patch('test_3_api.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'  # Assigning the mock_get_joke return value to one.
        self.assertEqual(len_joke(), 3, 'Not equal to length of joke')  # Testing the case using assertEqual method.

    @patch('test_3_api.get_joke')
    def test_original_len_joke(self, joke):
        joke.return_value = test_3_api.get_joke()
        print(joke.return_value)
        self.assertEqual(len_joke(), len(joke), 'length is not equal')


# Building mock classes


'''
monkeypatch.setattr can be used in conjunction with classes to mock returned objects from functions instead of values.
Use get_json function from the test_3_api module.
'''


class MockResponse:

    @staticmethod
    def json():
        return {'Mock_key': 'Mock_response'}


def test_get_json(monkeypatch):

    # Any argument may pass to the mock_get function only the MockResponse.json method will be called.
    def mock_get():
        return MockResponse()

    # apply monkeypatch to the requests.get method. When ever requests.get called it returns mock_get() method
    monkeypatch.setattr(requests, 'get', mock_get)

    # In test_3_api.py, a method called get_json which contains requests.get call will use the monkeypatch
    result = test_3_api.get_json("https://fakeurl")
    assert result['Mock_key'] == 'Mock_response'


""" We can use this mock class as pytest fixture for future uses. To do so, move the mock_get and monkeypatch.setattr
code lines to the conftest.py file and replace the monkeypatch with fixture name at the test_get_json function."""


def test1_get_json(mock_response):
    result = test_3_api.get_json('https://fakeurl')
    assert result['Mock_key'] == "Mock_response"
