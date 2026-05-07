import requests
from http import HTTPStatus
from api.auth_api import create_token

url = 'https://restful-booker.herokuapp.com/auth'

headers = {
  "Content-Type": 'application/json'
}

def test_post_request_with_correct_pass(client):
  response = create_token(client, "admin", "password123")

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.OK
  assert "token" in response.json()

def test_post_request_with_incorrect_pass(client):
  response = create_token(client, "admin", "nopass")

  print("Status Code", response.status_code)
  print("JSON Response ", response.json())

  assert response.status_code == HTTPStatus.BAD_REQUEST
  assert response.json()["reason"] == "Bad credentials"