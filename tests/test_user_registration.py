from src.conditions import status_code, body
from src.services import UserApiService
from hamcrest import has_length, greater_than


def test_user_can_register_with_valid_data(faker):
    user = {
        "username": faker.name(),
        "password": "12345",
        "email": faker.email()
    }

    response = UserApiService().create_user(user)

    response.should_have(status_code(200)) \
        .should_have(body("$.id", has_length(greater_than(0))))


def test_user_cannot_register_with_valid_data_twice(faker):
    user = {
        "username": faker.name(),
        "password": "12345",
        "email": faker.email()
    }
    userApiService = UserApiService()

    response = userApiService.create_user(user)
    response.should_have(status_code(200))
    response = userApiService.create_user(user)
    response.should_have(status_code(500))
