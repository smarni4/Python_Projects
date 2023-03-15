"""
Pytest fixture file:
            We can write the fixtures in one file named conftest to use the fixtures in multiple test files.
"""
# Global modules
import pytest

# Local modules
from data_file import Database, Student
import test_3_api
import test_4_mock


@pytest.fixture()
def assign_values1():
    a = 6
    b = 7
    c = 8
    return [a, b, c]


@pytest.fixture()
def supply_url():  # Supplies url when ever mentioned in the test case.
    return "https://regres.in/api"


@pytest.fixture()
def read_player(player_id):
    if player_id in Database.keys():
        data = Database[player_id]
        return {'Code': 200,
                'Response': {'Name': data[0], 'Team': data[1], 'Age': data[2], 'Score': data[3]},
                'Message': 'Player found'
                }
    return {'Code': 400, 'Message': 'Player does not exist.'}


@pytest.fixture()
def mock_response(monkeypatch):
    def mock_get():
        return test_4_mock.MockResponse()

    monkeypatch.setattr(test_3_api.requests, 'get', mock_get)


"""
   scope = class -> Uses same object value along the class tests
   scope = module -> Uses same object value along the module tests
   scope = function -> creates the object for every function.
"""


@pytest.fixture(scope='class', params=[('Python', 2.9), ('Python', 4.0)], ids=["Fail", "Pass"])
def student_object(request):    # Inbuilt request module & id's help to identify the test case
    s = Student('Veera', '1998/08/15', 'IT', request.param)
    return s


@pytest.fixture
def student_object_factory():
    def student(name, dob, branch, course):
        return Student(name, dob, branch, course)
    return student

