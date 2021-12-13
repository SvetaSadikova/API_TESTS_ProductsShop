import requests


class TestRegistration:
    def test_registration_with_valid_data(self, application):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        """
        # data = RegisterUser.random()
        data = {"username": "user5", "password": "pass5"}
        response = application.RegisterNewUser.registrationMethod(data=data)
        # assert response.data.message == ResponseText.MESSAGE_REGISTER_USER
        assert response.json().get('message') == "User created successfully."
        assert response.status_code == 201, "Check response"
