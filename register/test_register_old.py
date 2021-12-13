# import requests
#
#
# class TestRegister:
#     def test_register_valid_data(self):
#         url = 'https://stores-tests-api.herokuapp.com/register'
#         body = {"username": "user3", "password": "pass3"}
#         response = requests.post(url, json=body)
#         assert response.json().get('message') == "User created successfully."
#         assert response.json().get('uuid')
#         assert response.status_code == 201
#
#     def test_register_invalid_data(self):
#         url = 'https://stores-tests-api.herokuapp.com/register'
#         body = {"username": "user4"}
#         response = requests.post(url, json=body)
#         assert response.json().get('message').get('password') == 'This field cannot be blank.'
#         assert response.status_code == 400
