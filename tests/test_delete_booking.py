import requests
from http import HTTPStatus

auth_url = 'https://restful-booker.herokuapp.com/auth'
booking_url = 'https://restful-booker.herokuapp.com/booking'

headers = {
  "Content-Type": 'application/json'
}

def test_delete_booking_with_correct_token():
  # Authorise admin
  auth_data = {
  "username": "admin",
  "password": "password123"
  }

  response = requests.post(auth_url, headers=headers, json=auth_data)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  token = response.json()["token"]

  # Create booking
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
  response = requests.post(booking_url, headers=headers, json=request)

  booking_id = response.json()["bookingid"]


  del_url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
  del_header = {
    "Content-Type": 'application/json',
    "Cookie": f"token={token}"
  }

  response = requests.delete(del_url, headers=del_header, json=request)
  print("Status Code", response.status_code)

  assert response.status_code == HTTPStatus.CREATED

def test_delete_booking_without_token():
  # Authorise admin
  auth_data = {
  "username": "admin",
  "password": "password123"
  }

  response = requests.post(auth_url, headers=headers, json=auth_data)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  token = response.json()["token"]

  # Create booking
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
  response = requests.post(booking_url, headers=headers, json=request)

  booking_id = response.json()["bookingid"]


  del_url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
  del_header = {
    "Content-Type": 'application/json'
  }

  response = requests.delete(del_url, headers=del_header, json=request)
  print("Status Code", response.status_code)

  assert response.status_code == HTTPStatus.FORBIDDEN

def test_delete_booking_fake_token():
  # Authorise admin
  auth_data = {
  "username": "admin",
  "password": "password123"
  }

  response = requests.post(auth_url, headers=headers, json=auth_data)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  token = response.json()["token"]

  # Create booking
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
  response = requests.post(booking_url, headers=headers, json=request)

  booking_id = response.json()["bookingid"]


  del_url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
  del_header = {
    "Content-Type": 'application/json',
    "Cookie": f"token=FAKE123"
  }

  response = requests.delete(del_url, headers=del_header, json=request)
  print("Status Code", response.status_code)

  assert response.status_code == HTTPStatus.FORBIDDEN

def test_delete_other_booking_with_correct_token():
  # Authorise admin
  auth_data = {
  "username": "admin",
  "password": "password123"
  }

  response = requests.post(auth_url, headers=headers, json=auth_data)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  token = response.json()["token"]

  # Create booking
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
  response = requests.post(booking_url, headers=headers, json=request)

  booking_id = response.json()["bookingid"]


  del_url = f"https://restful-booker.herokuapp.com/booking/{booking_id+1}"
  del_header = {
    "Content-Type": 'application/json',
    "Cookie": f"token={token}"
  }

  response = requests.delete(del_url, headers=del_header, json=request)
  print("Status Code", response.status_code)

  assert response.status_code == HTTPStatus.CREATED