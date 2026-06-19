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
    "password": payload_create_user["password"]
}
response_login_user = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=payload_login_user)
login_user_data = response_login_user.json()
print(f"Authentication user (POST /authentication/login) data: {login_user_data}")

# 3. Удаляем пользователя
headers_delete_user = {"Authorization": f"Bearer {login_user_data['token']["accessToken"]}"}
response_delete_user = httpx.delete(
    url=f"http://localhost:8000/api/v1/users/{create_user_data["user"]['id']}",
    headers=headers_delete_user
)
print(f"Delete user (DELETE /users/:id), status cide: {response_delete_user.status_code}")