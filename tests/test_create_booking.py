import requests
from http import HTTPStatus
from api.booking_api import *

url = 'https://restful-booker.herokuapp.com/booking'

headers = {
  "Content-Type": 'application/json'
}

def test_create_booking_with_valid_bookingdates(client, cleanup_booking):
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

  response = create_booking(client, request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.OK
  assert "bookingid" in response.json()
  assert isinstance(response.json()["bookingid"], int)

  cleanup_booking.append(response.json()["bookingid"])

def test_create_booking_with_negative_totalprice(client, cleanup_booking):
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
  response = create_booking(client, request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.BAD_REQUEST

  cleanup_booking.append(response.json()["bookingid"])


def test_create_booking_with_invalid_totalprice(client, cleanup_booking):
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
  response = create_booking(client, request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.BAD_REQUEST

  cleanup_booking.append(response.json()["bookingid"])


def test_create_booking_with_empty_first_name(client, cleanup_booking):
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
  response = create_booking(client, request)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.BAD_REQUEST

  cleanup_booking.append(response.json()["bookingid"])

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
  assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

def test_create_booking_no_body():
  request = {}
  response = requests.post(url, headers=headers, json=request)

  print("Status Code", response.status_code)
  assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR