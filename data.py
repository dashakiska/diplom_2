import requests

from urls import Endpoints

class IngredientsData:
    @staticmethod
    def get_ingredient():
        response = requests.get(Endpoints.INGREDIENTS)
        return response.json()["data"][0]["_id"]
    
    @staticmethod
    def correct_ingredients_data():
        ingr_id = IngredientsData.get_ingredient()
        return {"ingredients": [ingr_id]}
    
    incorrect_ingredients_data = {"ingredients" : [ "70d3b41abd789b0026a73524", "709646e4dc916e00276kio53"]}