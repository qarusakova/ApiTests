import requests

class ApiClient:

  def __init__(self, base_url):
    self.base_url = base_url
    self.session = requests.Session()
    self.session.headers.update({"Content-Type": 'application/json'})

  def set_token(self, token):
    self.session.cookies.set("token", token)

  def remove_token(self):
    self.session.cookies.pop("token", None)

  def get(self, path, **kwargs):
    return self.session.get(f"{self.base_url}{path}", **kwargs)

  def post(self, path, **kwargs):
    return self.session.post(f"{self.base_url}{path}", **kwargs)

  def put(self, path, **kwargs):
    return self.session.put(f"{self.base_url}{path}", **kwargs)

  def delete(self, path, **kwargs):
    return self.session.delete(f"{self.base_url}{path}", **kwargs)