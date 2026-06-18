import  httpx

from tools.fakers import get_random_email


payload = {
    "email": get_random_email(),
    "password": "2556535",
    "lastName": "lastname",
    "firstName": "firstname",
    "middleName": "middlename"
}

response_create_user = httpx.post(url="http://localhost:8000/api/v1/users", json=payload)
print(response_create_user.status_code)
print(response_create_user.json())