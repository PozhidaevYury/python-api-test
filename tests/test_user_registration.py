from src.services import UserApiService


def test_user_can_register_with_valid_data(faker):
    user = {
        "username": faker.name(),
        "password": "12345",
        "email": "bob@gmail.com"
    }

    response = UserApiService().create_user(user)

    assert response.status_code == 200
    assert len(response.json()["id"]) > 0


def test_user_cannot_register_with_valid_data_twice(faker):
    user = {
        "username": faker.name(),
        "password": "12345",
        "email": "bob@gmail.com"
    }

    response = UserApiService().create_user(user)

    assert response.status_code == 200

    response = UserApiService().create_user(user)

    assert response.status_code == 500
