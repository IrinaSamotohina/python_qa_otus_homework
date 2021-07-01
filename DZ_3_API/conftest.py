import pytest
import requests


@pytest.fixture()
def dog_api_base_url():
    base_url='https://dog.ceo/api/'
    return base_url


@pytest.fixture()
def openbrewerydb_api_base_url():
    base_url='https://api.openbrewerydb.org/'
    return base_url


@pytest.fixture()
def jsonplace_api_base_url():
    base_url='https://jsonplaceholder.typicode.com/'
    return base_url


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default='https://ya.ru',
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        help="This is status code"
    )


@pytest.fixture()
def url_param(request):
    return request.config.getoption("--url")


@pytest.fixture()
def status_code_param(request):
    return request.config.getoption("--status_code")