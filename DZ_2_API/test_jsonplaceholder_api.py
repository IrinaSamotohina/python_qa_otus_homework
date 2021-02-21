import pytest
import requests
from random import randint


@pytest.mark.parametrize('path_value', [randint(1, 100)])
def test_json_api_1(jsonplace_api_base_url, path_value):
    path = f'posts/{path_value}'
    url = jsonplace_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize('data_value', [randint(1, 100)])
def test_json_api_2(jsonplace_api_base_url, data_value, path='posts'):
    jsonplace_api_data = {
            'title': f'New title {data_value}',
            'body': f'New body {data_value}',
            'userId': 1
        }
    url = jsonplace_api_base_url + path
    response = requests.post(url, data=jsonplace_api_data)
    assert response.status_code == 201
    assert response.json()['title'] == jsonplace_api_data['title']


def test_json_api_3(jsonplace_api_base_url, path='posts'):
    jsonplace_api_data = {
        "userId": 1,
        "id": 1}
    url = jsonplace_api_base_url + path
    response = requests.delete(url, data=jsonplace_api_data)
    assert response.status_code == 404

@pytest.mark.parametrize('path_value', [randint(1, 100)])
def test_json_api_4(jsonplace_api_base_url, path_value):
    path = f'posts/{path_value}'
    url = jsonplace_api_base_url + path
    response = requests.delete(url)
    assert response.status_code == 200


def test_json_api_5(jsonplace_api_base_url, path='posts/1'):
    jsonplace_api_data = {
        'id': 1,
        'title': 'New title after edit',
        'body': 'New body after edit',
        'userId': 1
        }
    url = jsonplace_api_base_url + path
    response = requests.put(url, data=jsonplace_api_data)
    assert response.status_code == 200