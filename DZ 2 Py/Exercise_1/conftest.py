import pytest


@pytest.fixture
def list_test():
    list_for_1 = [1, 2, 4, "a", "b", "c", "d", {"all": "dict"}]
    return list_for_1


@pytest.fixture(scope="function")
def dict_test():
    dict_for_1 = {
        "_id": "5e2696e561fdc6df60d43b5f",
        "index": 0,
        "isActive": False,
        "guid": "3e518b31-20f0-4dea-8de8-039af5afbd33",
        "balance": "$3,646.47",
        "picture": "http://placehold.it/32x32",
        "age": 34,
        "eyeColor": "brown",
        "name": "Lolita Lynn",
        "gender": "female",
        "company": "HIVEDOM",
        "email": "lolitalynn@hivedom.com",
        "phone": "+1 (842) 513-2979",
        "address": "389 Neptune Avenue, Belfair, Iowa, 6116",
        "latitude": 0.246756,
        "longitude": -96.404056
    }
    return dict_for_1


@pytest.fixture
def set_test_1():
    data_for_test = ["name", "parameters", "location", "role", "race", "sets"]
    set_for_1 = set(data_for_test)
    return set_for_1


@pytest.fixture
def set_test_2():
    data_for_test = ["name", "parameters", "location", "role", "race", "sets"]
    set_for_2 = set(data_for_test)
    return set_for_2


@pytest.fixture()
def string_1():
    data_string_1 = 'qwertyuiop[]!'
    return data_string_1


@pytest.fixture()
def string_2():
    data_string_2 = 'qwertyuiop[]!'
    return data_string_2