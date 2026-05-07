import pytest

from api.api_client import ApiClient
from api.auth_api import create_token
from api.booking_api import delete_booking
from config import BASE_URL

@pytest.fixture
def client():
  return ApiClient(BASE_URL)

@pytest.fixture
def auth_token(client):
  response = create_token(client)
  return response.json()["token"]

@pytest.fixture
def cleanup_booking(client, auth_token):
  booking_ids = []
  yield booking_ids
  for booking_id in booking_ids:
        delete_booking(client, booking_id, auth_token)