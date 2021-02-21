import pytest
import requests
from random import randint


def test_openbrewerydb_api_1(openbrewerydb_api_base_url, path='/breweries'):
    url = openbrewerydb_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200


def test_openbrewerydb_api_2(openbrewerydb_api_base_url, path='/breweries/search?query=dog'):
    url = openbrewerydb_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200


def test_openbrewerydb_api_3(openbrewerydb_api_base_url, path='/breweries/autocomplete?query=dog'):
    url = openbrewerydb_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize(['static_path_value', 'dynamic_path_value', 'response_result'],
                         [('breweries?by_city=', 'san_diego', 'San Diego'),
                          ('breweries?by_city=', 'san%20diego', 'San Diego'),
                          ('breweries?by_city=', 'tucson', 'Tucson'),
                          ('breweries?by_city=', 'los%20angeles', "Los Angeles")])
def test_openbrewerydb_api_3(openbrewerydb_api_base_url, static_path_value, dynamic_path_value, response_result):
    path = f'{static_path_value}/{dynamic_path_value}'
    url = openbrewerydb_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200
    for i in response.json():
        assert response.json()[i]["city"] == response_result


@pytest.mark.parametrize('path_value', [randint(1, 6000)])
def test_openbrewerydb_api_4(openbrewerydb_api_base_url, path_value):
    path = f'/breweries/{path_value}'
    url = openbrewerydb_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'brewery_type' in response.json()
    assert 'county_province' in response.json()
    assert 'street' in response.json()
    assert 'postal_code' in response.json()
    assert 'longitude' in response.json()
    assert 'website_url' in response.json()