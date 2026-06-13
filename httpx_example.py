import httpx

# from pprint import pprint


# Выполнение GET запроса
response = httpx.get(url="http://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

# Выполнение POST запроса. Передаем в качестве аргумента json Python-словарь
data = {
    "userId": 111,
    "title": "Test title",
    "completed": True
}
response = httpx.post(url="http://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())

# Выполнение POST запроса. Отправка данных в application/x-www-form-urlencoded. Передаем через аргумент data
data = {
    "first_name": "test_first_name",
    "last_name": "test_last_name"
}
response = httpx.post(url="https://httpbin.org/post", data=data)
print(response.status_code)
# pprint(response.json())
print(response.json())

# Выполнение GET запроса с передачей кастомных заголовков. Передаем через аргумент headers
headers = {
    "Authorization": "Bearer custom_test_token"
}
response = httpx.get(url="https://httpbin.org/get", headers=headers)
print(response.status_code)
print(response.request.headers)
# pprint(response.json())
print(response.json())

# Выполнение GET запроса с path параметрами. Метод params добавляет параметры к URL, аналогично ?key=value
params = {
    "userId": 3
}
response = httpx.get(url="https://jsonplaceholder.typicode.com/todos", params=params)
print(response.request.url)
print(response.status_code)
print(response.json())

# Отправка файлов
files = {
    "file": ("test.txt",open("test.txt", "rb"))
}
response = httpx.post(url="https://httpbin.org/post", files=files)
print(response.status_code)
print(response.json())

# Работа с сессиями (httpx.Client), который повторно использует соединения
with httpx.Client() as client:
    response1 = client.get(url="https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get(url="https://jsonplaceholder.typicode.com/todos/2")
    response3 = client.get(url="https://jsonplaceholder.typicode.com/todos/3")

print(response1.status_code)
print(response1.json())
print(response2.status_code)
print(response2.json())
print(response3.status_code)
print(response3.json())

# Добавление базовых заголовков в Client
client = httpx.Client(
    headers={
        "Authorization": "Bearer custom_client_test_token"
    }
)
response = client.get(url="https://httpbin.org/get")
print(response.request.headers)
print(response.status_code)
print(response.json())

# Работа с ошибками. Проверка статуса ответа (raise_for_status)
try:
    response = httpx.get(url="https://jsonplaceholder.typicode.com/expected-404")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

# Работа с ошибками. Обработка таймаутов
try:
    response = httpx.get(url="https://httpbin.org/delay/5", timeout=1)
    response.raise_for_status()
except httpx.ReadTimeout:
    print("Запрос превысил установленный лимит времени")