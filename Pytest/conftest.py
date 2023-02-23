"""
Pytest fixture file:
            We can write the fixtures in one file named conftest to use the fixtures in multiple test files.
"""

import pytest


@pytest.fixture()
def assign_values1():
    a = 6
    b = 7
    c = 8
    return [a, b, c]
