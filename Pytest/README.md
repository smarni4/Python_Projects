In this PyTest tutorial, we covered

* Install pytest using pip install pytest
* Simple pytest program and run it with pytest command.
* Assertion statements, assert x==y, will return either True or False.
* How pytest identifies test files and methods.
    * Test files starting with test_ or ending with _test
    * Test methods starting with test
* py.test command will run all the test files in that folder and sub-folders. To run a specific file, we can use the command pytest <filename>
* Run a subset of test methods
    * Grouping of test names by substring matching.py.test -k <name> -v will run all the tests having <name> in its name.
    * Run test by markers.Mark the tests using @pytest.mark.<name> and run the tests using pytest -m <name> to run tests marked as <name>.
* Run tests in parallel
    * Install pytest-xdist using pip install pytest-xdist
    * Run tests using pytest -n NUM where NUM is the number of workers
* Creating fixture methods to run code before every test by marking the method with @pytest.fixture
    * The scope of a fixture method is within the file it is defined.
    * A fixture method can be accessed across multiple test files by defining it in conftest.py file.
    * A test method can access a Pytest fixture by using it as an input argument.
* Parametrizing tests to run it against multiple set of inputs.
@pytest.mark.parametrize(“input1, input2, output”,[(5,5,10),(3,5,12)])
def test_add(input1, input2, output):
assert input1+input2 == output, ” failed ”
will run the test with inputs (5,5,10) and (3,5,12)
* Skip/xfail tests using @pytest.mark.skip and @pytest.mark.xfail
* Create test results in XML format which covers executed test details using pytest test_sample1.py -v –junitxml=”result.xml”
* A sample pytest framework to test an API
* Documenting the code using sphinx-documentation
  *  First create the environment using python -m venv .venv
  *  Next assign the source using source .venv/bin/activate
  *  Install the sphinx using pip install sphinx
  *  Now create the required doc files using sphinx-quickstart docs
  *  For the first time run sphinx-build -b html docs/source/ docs/build/html

