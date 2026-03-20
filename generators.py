from faker import Faker

fake = Faker('ru_RU')

def generate_fake_data():
    return {
        "email": Faker().email(),
        "password": Faker().password(length=10),
        "name": fake.first_name(),}