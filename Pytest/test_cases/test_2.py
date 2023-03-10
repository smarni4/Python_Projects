import json
import os
import pytest

from data_file import save_dict, get_topper, students, is_eligible_for_degree

"""
Pytest Fixture:
    Fixtures are used when we need to run a code before every test. To do so we need to create a code that we want to 
    run before test and decorate it with the @pytest.fixture. Now, when ever we need to run that code before tests we
    have to pass the fixture function name as a variable to that test.
    
    We can only use the fixture inside this file, if we want to use the fixture in multiple files we have to write the 
    fixture in conftest.py file. The pytest library will first look for the fixture inside the file if it can't find 
    the fixture it will look in the conftest file located in the project folder.
    
    We can also create temporary files and directories required to test the functions and assign their paths to the
    respective functions using pytest fixtures. There are some builtin fixture variables to do so such as
    
    - capfd
        Capture, as text, output to file descriptors 1 and 2.

    - capfdbinary
        Capture, as bytes, output to file descriptors 1 and 2.

    - caplog
        Control logging and access log entries.

    - capsys
        Capture, as text, output to sys.stdout and sys.stderr.

    - capsysbinary
        Capture, as bytes, output to sys.stdout and sys.stderr.

    - cache
        Store and retrieve values across pytest runs.

    - doctest_namespace
        Provide a dict injected into the docs tests namespace.

    - monkeypatch
        Temporarily modify classes, functions, dictionaries, os.environ, and other objects.

    - pytestconfig
        Access to configuration values, pluginmanager and plugin hooks.

    - record_property
        Add extra properties to the test.

    - record_testsuite_property
        Add extra properties to the test suite.

    - recwarn
        Record warnings emitted by test functions.

    - request
        Provide information on the executing test function.

    - testdir
        Provide a temporary test directory to aid in running, and testing, pytest plugins.

    - tmp_path
        Provide a pathlib.Path object to a temporary directory which is unique to each test function.

    - tmp_path_factory
        Make session-scoped temporary directories and return pathlib.Path objects.

    - tmpdir
        Provide a py.path.local object to a temporary directory which is unique to each test function;
        replaced by tmp_path.

    - tmpdir_factory
        Make session-scoped temporary directories and return py.path.local objects; replaced by tmp_path_factory.
    
"""


@pytest.fixture
def assign_values():  # fixture inside the file
    a = 5
    b = 6
    c = 7
    return [a, b, c]


def test_case2_1(assign_values):
    assert assign_values[0] == 6, 'assign_values[0] is not equal to 6.'


def test_case2_2(assign_values1):  # fixture inside the conftest file.
    assert assign_values1[0] == 7, 'assign_values1[0] is not equal to 6.'


def test_case2_3(assign_values):
    assert assign_values[0] > 6, 'assign_values[0] is less than 6.'


def test_case2_4(capsys, tmpdir='../testfolder'):  # We can assign the temporary path to the tmpdir variable
    filepath = os.path.join(tmpdir, "test_dict.json")  # capsys will read the error or sys.out value
    _dict = {'a': 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict, "tmp_dir test failed"
    assert capsys.readouterr().out == '\n saved\n', "print line is not printing saved"


class Test_student:
    """  Using fixture scope """
    def test_case2_5(self, student_object):  # Student class test
        assert student_object.get_age() == 24, 'Age function is not working'

    def test_case2_6(self, student_object):

        assert student_object.get_credits() == {'Python': 3.0}, 'credits is not equal to 3.0'

    def test_case2_7(self, student_object):
        student_object.add_credit('Python', 4.0)
        assert student_object.get_credits() == {'Python': 4.0}, 'Get credits is not working'

    # def test_case2_8(self, student_object):
    #     assert student_object.get_credits() == {}, 'This will fail because the get credits will return '\
    #                                                '{"Python": 4.0} as the fixture is being used under class scope'

    """ Using fixture factory """
    def test_case2_9(self, student_object_factory):
        assert get_topper(students) == ('Venkata', 4.5), 'get_topper function is not working'


""" We can use a fixture as a param of fixture using the indirect function of the fixture. """
@pytest.mark.parametrize("student_object, expected", [(('Python', 19), False), (('Python', 21), True)],
                         indirect=['student_object'])
def test_case2_10(student_object, expected):
    assert is_eligible_for_degree(student_object) is expected
