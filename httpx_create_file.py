import httpx

from tools.fakers import get_random_email


# 1. Создаем пользователя методом POST /api/v1/users
payload_create_user = {
    "email": get_random_email(),
    "password": "2556535",
    "lastName": "lastname",
    "firstName": "firstname",
    "middleName": "middlename"
}

response_create_user = httpx.post(
    url="http://localhost:8000/api/v1/users",
    json=payload_create_user
)
create_user_data = response_create_user.json()
user_id = create_user_data["user"]["id"]
print(f"Status code: {response_create_user.status_code}")
print(f"Create user (POST /users) data: {create_user_data}")

# 2. Проходим аутентификацию методом POST /api/v1/authentication/login
payload_login_user = {
    "email": payload_create_user["email"],
    "password": payload_create_user["password"]
}
response_login_user = httpx.post(
    url="http://localhost:8000/api/v1/authentication/login",
    json=payload_login_user
)
login_user_data = response_login_user.json()
access_token = login_user_data["token"]["accessToken"]
print(f"Status code: {response_login_user.status_code}")
print(f"Authentication user (POST /authentication/login) data: {login_user_data}")

create_file_headers = {
    "Authorization": f"Bearer {access_token}"
}
response_create_file = httpx.post(
    url="http://localhost:8000/api/v1/files",
    data={"filename": "image.png", "directory": "courses_directory"},
    files={"upload_file": open("testdata/files/image.png", "rb")},
    headers=create_file_headers
)
create_file_data = response_create_file.json()
print(f"Status code: {response_create_file.status_code}")
print(f"Create file (POST /files) data: {create_file_data}")