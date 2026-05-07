import requests
from http import HTTPStatus

url = 'https://restful-booker.herokuapp.com/auth'

headers = {
  "Content-Type": 'application/json'
}

def test_post_request_with_correct_pass():
  auth_data = {
  "username": "admin",
  "password": "password123"
  }
  response = requests.post(url, headers=headers, json=auth_data)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.OK
  assert "token" in response.json()

def test_post_request_with_incorrect_pass():
  auth_data = {
  "username": "admin",
  "password": "nopass"
}
  response = requests.post(url, headers=headers, json=auth_data)

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.BAD_REQUEST
  assert response.json()["reason"] == "Bad credentials"