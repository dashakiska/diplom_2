import allure
import pytest
import requests

from urls import Endpoints
from generators import generate_fake_data
from conftest import create_user_fixt

class TestLoginUser:
    @allure.title("вход под существующим пользователем")
    def test_login_existing_user_success(self, create_user_fixt):
        data, access_token = create_user_fixt

        with allure.step("Отправка POST запроса на вход пользователя"):
            response = requests.post(Endpoints.LOGIN, json=data)

        with allure.step("Получение в ответе кода 200"):
            assert response.status_code == 200 and response.json()["success"] is True and "accessToken" in response.json() and "refreshToken" in response.json()    

    def test_login_with_incorrect_username_and_password_fail(self):
        data = {"email": "hello@mail.com", "password": "hello123"}

        with allure.step("Отправка POST запроса на вход пользователя"):
            response = requests.post(Endpoints.LOGIN, json=data)

        with allure.step("Получение в ответе кода 401"):
            assert response.status_code == 401 and response.json()["success"] is False and response.json()["message"] == "email or password are incorrect"      


      





