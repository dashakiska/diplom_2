import allure
import pytest
import requests

from urls import Endpoints
from generators import generate_fake_data

class TestCreateUser:

    @allure.title("создание уникального пользователя")
    def test_create_unique_user_success(self):
        data = generate_fake_data()

        with allure.step("Отправка POST запроса на создание пользователя"):
            response = requests.post(Endpoints.REGISTER, json=data)

        with allure.step("Получение в ответе кода 200"):
            assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("создание пользователя, который уже зарегистрирован") 
    def test_create_duplicate_user_fail(self):
        data = generate_fake_data()
        
        with allure.step("Отправка POST запроса на создание пользователя"):
            requests.post(Endpoints.REGISTER, json=data)

        with allure.step("Отправка POST запроса на создание того же пользователя повторно"):
            response = requests.post(Endpoints.REGISTER, json=data)    

        with allure.step("Получение в ответе кода 403"): 
            assert response.status_code == 403 and response.json()["success"] is False and response.json()["message"] == "User already exists"  

    @allure.title("создание пользователя при пустом поле пароль") 
    def test_create_user_without_password_fail(self):
        data = generate_fake_data()

        with allure.step("удаление пароля"):
            data.pop("password")

        with allure.step("Отправка POST запроса на создание пользователя"):
            response = requests.post(Endpoints.REGISTER, json=data)

        with allure.step("Получение в ответе кода 403"): 
            assert response.status_code == 403 and response.json()["success"] is False and response.json()["message"] == "Email, password and name are required fields"          









