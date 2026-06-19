import httpx

from tools.fakers import get_random_email


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
print(f"Create user data: {create_user_data}")

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

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=10, # в секундах
    headers={"Authorization": f"Bearer {access_token}"},
)
response_get_user_me = client.get(url="/api/v1/users/me")
get_user_me_data = response_get_user_me.json()
print(f"Get user me data: {get_user_me_data}")
response_get_user_by_id = client.get(url=f"/api/v1/users/{user_id}")
get_user_by_id_data = response_get_user_by_id.json()
print(f"Get user by id data: {get_user_by_id_data}")
