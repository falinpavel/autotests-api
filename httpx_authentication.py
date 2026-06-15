import httpx

# Тело запроса POST /authentication/login со своими данными пользователя
login_payload = {
    "email": "123@yandex.ru",
    "password": "2556535",
}
# Выполняем запрос, передаем свой payload
login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=login_payload)
print(f"Статус код: {login_response.status_code}")
print(f"Тело ответа: {login_response.json()}")
# Сохраняем в переменную refresh токен
refresh_token = login_response.json()["token"]["refreshToken"]

# Тело запроса POST /authentication/refresh
refresh_payload = {
    "refreshToken": refresh_token
}
# Выполняем запрос, передаем свой payload с ранее полученным refresh токеном
refresh_response = httpx.post(url="http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
print(f"Статус код: {refresh_response.status_code}")
print(f"Тело ответа: {refresh_response.json()}")