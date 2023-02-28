import pytest

''' Using pytest we can test single or multiple tests at a time. It detects the test cases based on the function names
    or class names. Usually pytest test cases will start or end with word test_ or _test.'''


def inc(x):
    return x + 1


def raise_error():
    raise SystemExit("print raised an error")


@pytest.mark.basic
@pytest.mark.odd  # mark function helps to run partial tests in the file, Here we used odd and even as markers.
def test_case1_1():
    assert inc(4) == 6, "test failed"


@pytest.mark.basic
@pytest.mark.even
def test_case1_2():
    with pytest.raises(SystemExit):
        raise_error()


class TestClass:
    x = 'this'

    @pytest.mark.odd
    def test_case1_3(self):
        assert 'h' in self.x

    @pytest.mark.even
    def test_case1_4(self):
        name = 'Veera'
        assert 'V' in name


@pytest.mark.odd
def test_case1_5():
    assert hasattr(TestClass, 'x')


''' We can run the multiple tests in parallel to reduce the execution time, using pytest-xdist module. To do that we 
    need to install it by running the command pip install pytest-xdist.
    
    We can distribute the tests to the workers using the file name or group name we assigned to te test using decorator
    by mentioning the format in the command line
    
    --dist load : Sends pending tests to any worker that is available, without any guaranteed order.
    
    --dist loadscope : Tests are grouped by module for test functions and by class for test methods.
    
    --dist loadfile : Tests are grouped by their containing file. Groups are distributed to available
                      workers as whole units
    
        Example command: pytest -k test_ --dist loadfile test_1.py test_2.py test_3_api.py

    --dist loadgroup : Tests are grouped by the xdist_group mark. Groups are distributed to available
                       workers as whole units.
    
        Example command:  pytest test_1.py --dist loadgroup group1 '''


@pytest.mark.xdist_group('group1')
def test_case1_6():
    x = 4
    assert x+1 == 6, 'group1 test_case'


@pytest.mark.xdist_group('group2')
def test_case1_7():
    x = 5
    assert x+1 == 6, 'group2 test_case'


@pytest.mark.xdist_group(name="group1")
def test_case1_8():
    x = 8
    assert x+2 == 9, 'group1 test_case'


@pytest.mark.xdist_group(name="group2")
def test_case1_9():
    x = 10
    assert x*10 == 110, 'group2 test_case'


'''
Pytest Parameterized Test:
    The purpose of parameterized test is to run a test against multiple arguments.

In the test case 1_10 input1, input2, and output are assigned as arguments and two sets of data are passed. This test 
will add the first two values of each set and check the result with third value in the respective set.
'''


@pytest.mark.parametrize("input1, input2, output", [(5, 3, 8), (7, 0, 17)])
def test_case1_10(input1, input2, output):
    assert input1+input2 == output, 'test failed'


'''
Pytest Xfail/Skip tests:
    This function is useful when we dont want to run the test or we dont want to consider the test fail status while
    running multiple tests.
    
    skip: It skips the tests.
    Xfail: It provide any output even the test failed.
    '''


@pytest.mark.skip
def test_case1_11():
    assert 100 + 200 == 500, 'test skip failed'


@pytest.mark.skip
def test_case1_12():
    assert 100 + 200 == 300, 'test skip will pass'


@pytest.mark.xfail
def test_case1_13():
    assert 100 + 400 == 500, 'test will pass'


@pytest.mark.xfail
def test_case1_14():
    assert 100 + 400 == 600, 'test will fail'


'''
To generate a xml file for the test results run the command
    pytest <test_file> -v --junitxml="<xml_file_name>" 
'''
