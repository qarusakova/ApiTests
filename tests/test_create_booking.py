import requests
import pytest
from http import HTTPStatus

url = 'https://restful-booker.herokuapp.com/booking'

headers = {
  "Content-Type": 'application/json'
}

@pytest.mark.skip(reason="too much requests on this record")
def test_create_booking_with_valid_bookingdates():
  request = {
  "firstname": "Inna",
  "lastname": "Test",
  "totalprice": 150,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2026-05-01",
    "checkout": "2026-05-05"
    }
  }
  response = requests.post(url, headers=headers, json=request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.OK
  assert "bookingid" in response.json()
  assert isinstance(response.json()["bookingid"], int)

@pytest.mark.skip(reason="too much requests on this record")
def test_create_booking_with_negative_totalprice():
  request = {
  "firstname": "Inna",
  "lastname": "Test",
  "totalprice": -150,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2026-05-01",
    "checkout": "2026-05-05"
    }
  }
  response = requests.post(url, headers=headers, json=request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.BAD_REQUEST

@pytest.mark.skip(reason="too much requests on this record")
def test_create_booking_with_invalid_totalprice():
  request = {
  "firstname": "Inna",
  "lastname": "Test",
  "totalprice": "сто",
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2026-05-01",
    "checkout": "2026-05-05"
    }
  }
  response = requests.post(url, headers=headers, json=request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  #assert response.status_code == HTTPStatus.BAD_REQUEST

@pytest.mark.skip(reason="too much requests on this record")
def test_create_booking_with_empty_first_name():
  request = {
  "firstname": "",
  "lastname": "Test",
  "totalprice": 150,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2026-05-01",
    "checkout": "2026-05-05"
    }
  }
  response = requests.post(url, headers=headers, json=request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  #assert response.status_code == HTTPStatus.BAD_REQUEST

def test_create_booking_without_firstname():
  request = {
  "lastname": "Test",
  "totalprice": 150,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2026-05-01",
    "checkout": "2026-05-05"
    }
  }
  response = requests.post(url, headers=headers, json=request)

  print("Status Code", response.status_code)

def test_create_booking_no_body():
  request = {}
  response = requests.post(url, headers=headers, json=request)

  print("Status Code", response.status_code)