import allure
import pytest
import requests

from urls import Endpoints
from generators import generate_fake_data
from data import IngredientsData
from conftest import create_user_fixt

class TestCreateOrder:
    @allure.title("создание заказа с авторизацией")
    def test_create_order_with_auth_success(self, create_user_fixt):
        data, access_token = create_user_fixt
        headers = {"Authorization": access_token}

        with allure.step("получение ингредиентов"):
            order_data = IngredientsData.correct_ingredients_data()        

        with allure.step("Отправка POST запроса на создание заказа"):
            response = requests.post(Endpoints.CREATE_ORDER, json=order_data, headers=headers)

        with allure.step("Получение в ответе кода 200"):
            assert response.status_code == 200 and response.json()["success"] is True 

    @allure.title("создание заказа без авторизации")
    def test_create_order_without_auth_success(self):

        with allure.step("получение ингредиентов"):
            order_data = IngredientsData.correct_ingredients_data()

        with allure.step("Отправка POST запроса на создание заказа"):
            response = requests.post(Endpoints.CREATE_ORDER, json=order_data)

        with allure.step("Получение в ответе кода 200"):
            assert response.status_code == 200 and response.json()["success"] is True    

    @allure.title("создание заказа с ингредиентами")
    def test_create_order_with_ingredients_success(self): 

        with allure.step("получение ингредиентов"):
            order_data = IngredientsData.correct_ingredients_data()

        with allure.step("Отправка POST запроса на создание заказа с ингредиентами"):
            response = requests.post(Endpoints.CREATE_ORDER, json=order_data)     

        with allure.step("Получение в ответе кода 200"):
            assert response.status_code == 200 and response.json()["success"] is True and "order" in response.json()

    @allure.title("создание заказа без ингредиентов")
    def test_create_order_without_ingredients_fail(self): 
        without_ing = {"ingredients":[]}   

        with allure.step("Отправка POST запроса на создание заказа без ингредиентов"):
            response = requests.post(Endpoints.CREATE_ORDER, json=without_ing) 

        with allure.step("Получение в ответе кода 400"):
            assert response.status_code == 400 and response.json()["success"] is False and response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("создание заказа с неверным хешем ингредиентов")
    def test_create_order_incorrect_hash_ingredients_fail(self): 

        with allure.step("Отправка POST запроса на создание заказа с неверным хешем ингредиентов"):
            response = requests.post(Endpoints.CREATE_ORDER, json=IngredientsData.incorrect_ingredients_data)     

        with allure.step("Получение в ответе кода 500"):
            assert response.status_code == 500 



                 
