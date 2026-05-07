def create_token(client, username="admin", password="password123"):
  return client.post("/auth", json={
      "username": username,
      "password": password
    }
  )