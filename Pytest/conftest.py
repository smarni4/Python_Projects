"""
Pytest fixture file:
            We can write the fixtures in one file named conftest to use the fixtures in multiple test files.
"""

import pytest

import data_file
import test_3_api


@pytest.fixture()
def assign_values1():
    a = 6
    b = 7
    c = 8
    return [a, b, c]


@pytest.fixture()
def supply_url():       # Supplies url when ever mentioned in the test case.
    return "https://regres.in/api"


@pytest.fixture()
def read_player(player_id):
    if player_id in data_file.Database.keys():
        data = data_file.Database[player_id]
        return {'Code': 200,
                'Response': {'Name': data[0], 'Team': data[1], 'Age': data[2], 'Score': data[3]},
                'Message': 'Player found'
                }
    return {'Code': 400, 'Message': 'Player does not exist.'}
