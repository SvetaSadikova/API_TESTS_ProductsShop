import requests
from requests import Response


class Registration:
    def __init__(self, app):
        self.MyApp = app

    POST_REGISTRATION = '/register'

    def registrationMethod(self, data) -> Response:
        return requests.post(f"{self.MyApp.MyUrl}{self.POST_REGISTRATION}", json=data)
