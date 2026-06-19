import httpx

from tools.fakers import get_random_email


# 1. Создаем пользователя
payload_create_user = {
    "email": get_random_email(),
    "password": "2556535",
    "lastName": "lastname",
    "firstName": "firstname",
    "middleName": "middlename"
}

response_create_user = httpx.post(url="http://localhost:8000/api/v1/users", json=payload_create_user)
create_user_data = response_create_user.json()
print(f"Create user (POST /users) data: {create_user_data}")

# 2. Логинимся под ранее зарегистрированным пользователем
payload_login_user = {
    "email": payload_create_user["email"],
    "password": payload_create_user["password"],
}
response_login_user = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=payload_login_user)
authentication_user_data = response_login_user.json()
print(f"Authentication user (POST /authentication/login) data: {authentication_user_data}")

# 3. Получаем данные о своем пользователе
with httpx.Client(headers={"Authorization": f"Bearer {response_login_user.json()["token"]["accessToken"]}"}) as client:
    response_get_user_me = client.get(url="http://localhost:8000/api/v1/users/me")
    get_user_me_data = response_get_user_me.json()
    assert response_get_user_me.status_code == httpx.codes.OK
    assert get_user_me_data["user"]["email"] == payload_create_user["email"]
    assert get_user_me_data["user"]["lastName"] == payload_create_user["lastName"]
    assert get_user_me_data["user"]["firstName"] == payload_create_user["firstName"]
    assert get_user_me_data["user"]["middleName"] == payload_create_user["middleName"]
    print(f"Get user me (GET /users/me) data: {get_user_me_data}")

    response_get_user_by_id = client.get(
        url=f"http://localhost:8000/api/v1/users/{create_user_data["user"]["id"]}"
    )
    get_user_by_id_data = response_get_user_by_id.json()
    assert response_get_user_by_id.status_code == httpx.codes.OK
    assert get_user_by_id_data["user"]["email"] == payload_create_user["email"]
    print(f"Get user by id (GET /users/:id) data: {get_user_by_id_data}")