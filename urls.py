class Endpoints:
    BASE_URL = "https://stellarburgers.education-services.ru"

    REGISTER = f"{BASE_URL}/api/auth/register"
    LOGIN = f"{BASE_URL}/api/auth/login" #для авторизации
    CREATE_ORDER = f"{BASE_URL}/api/orders"
    INGREDIENTS = f"{BASE_URL}/api/ingredients"
    USER_ORDER = f"{BASE_URL}/api/orders"
    DELETE_USER = f"{BASE_URL}/api/auth/user"
