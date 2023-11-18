import requests

BASE_URL = "http://127.0.0.1:5000/"


def test_weather_get_with_name():

    params = {'nome': 'Washington'}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200


def test_weather_get_with_name_and_city():
    BASE_URL + "Manaus"
    params = {'nome': 'Washington'}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200


def test_weather_post():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
