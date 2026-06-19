import httpx

# 1. Тело запроса POST /authentication/login, в email и password передаем данные своего пользователя
login_payload = {
    "email": "123@yandex.ru",
    "password": "2556535"
}
# 2. Выполняем запрос, передаем свой payload в json
login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=login_payload)

# 3. Сохраняем accessToken в переменную
access_token = login_response.json()["token"]["accessToken"]

# 4. Выполняем запрос GET /users/me, используя ранее полученный accessToken в ответе метода POST /authentication/login
with httpx.Client(headers={"Authorization": f"Bearer {access_token}"}) as client:
    users_me_response = client.get(url="http://localhost:8000/api/v1/users/me")
    print(f"Статус код ответа: {users_me_response.status_code}")
    print(f"Тело ответа: {users_me_response.json()}")
