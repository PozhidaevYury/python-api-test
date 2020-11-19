from src.services import UserApiService


def test_user_can_register_with_valid_data(faker):
    user = {
        "username": faker.name(),
        "password": "12345",
        "email": faker.email()
    }

    response = UserApiService().create_user(user)

    assert response.status_code(200)
    assert len(response.field("id")) > 0


def test_user_cannot_register_with_valid_data_twice(faker):
    user = {
        "username": faker.name(),
        "password": "12345",
        "email": faker.email()
    }
    userApiService = UserApiService()

    response = userApiService.create_user(user)

    assert response.status_code(200)

    response = userApiService.create_user(user)

    assert response.status_code(500)
