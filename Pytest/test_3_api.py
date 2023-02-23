"""
In this file we will perform tests on an API. THe api we are using is taken from https://reqres.in/. We are writing 
some tests for listing some users and login with users.

To do that, first we need to create a fixture inside conftest file which will supply base url for all the tests.
"""

import pytest
import requests
import json


@pytest.mark.users
@pytest.mark.parametrize("userid, first_name", [(7, 'Michael'), (8, 'Lindsay')])    # Runs test for the given two inputs
def test_valid_users(supply_url, userid, first_name):       # used fixture from the conftest file
    url = supply_url + '/users/' + str(userid)
    resp = requests.get(url)
    print(resp.text)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['data']['id'] == userid, resp.text
    assert j['data']['first_name'] == first_name, resp.text


@pytest.mark.users
def test_invalid_users(supply_url):
    url = supply_url + '/users/50'
    resp = requests.get(url)
    assert resp.status_code == 404, resp.text


player_id_list = ['1', '3', '2', '4', '5']


@pytest.mark.players
@pytest.mark.parametrize('player_id', player_id_list)
def test_read_player(read_player, player_id):
    # resp = read_player(player_id)
    assert read_player["Code"] == 200, 'player not found'
