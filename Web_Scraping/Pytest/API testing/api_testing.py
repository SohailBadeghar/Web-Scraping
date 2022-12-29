import pytest
import requests
import json


def test_valid_login():

    # Taken testing api of login successful from "https://reqres.in/" .
    url = "https://reqres.in/api/login"

    # This is wrong credential given to check the status code response it will fail the test.
    # data = {
    #     'email':'abc@gmail.com',
    #     'password':'abc123'
    # }

    # This is correct credential given to check the status code response it will Passed the test with correct data.
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    # Posting the url and data using request module on Browser.
    response = requests.post(url, data=data)
    token = json.loads(response.text)

    # it will check whether incoming response matches the 200 ok response.
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"
