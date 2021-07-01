import pytest
import requests

def test_status_code(url_param, status_code_param):
    response = requests.get(url_param).status_code
    assert str(response) == status_code_param
