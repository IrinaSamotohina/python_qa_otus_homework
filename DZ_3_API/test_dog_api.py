import pytest
import requests
from random import randint


def test_dog_api_1(dog_api_base_url, path='breeds/list/all'):
    url = dog_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200


def test_dog_api_2(dog_api_base_url, path='breeds/image/random'):
    url = dog_api_base_url + path    
    response = requests.get(url)
    assert response.status_code == 200


def test_dog_api_3(dog_api_base_url, path='breeds/image/random'):
    url = dog_api_base_url + path
    response = requests.get(url)
    assert 'message' in response.json()


@pytest.mark.parametrize('path_value', ['corgi/cardigan', 'boxer', 'doberman'])
def test_dog_api_4(dog_api_base_url, path_value):
    path = f'breed/{path_value}/images/random'
    url = dog_api_base_url + path    
    response = requests.get(url)
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize('path_value', [randint(1, 50)])
def test_dog_api_5(dog_api_base_url, path_value):
    path = f'breeds/image/random/{path_value}'
    url = dog_api_base_url + path
    response = requests.get(url)
    assert response.status_code == 200

