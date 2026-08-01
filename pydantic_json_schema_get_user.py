from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema

from tools.fakers import fake

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()
# Инициализируем запрос на создание пользователя
create_users_request = CreateUserRequestSchema(
    email=fake.email(),
    password="password",
    last_name="lastname",
    first_name="firstname",
    middle_name="middlename"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(request=create_users_request)
# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_users_request.email,
    password=create_users_request.password
)

# Инициализируем клиент PublicUsersClient
private_users_client = get_private_users_client(user=authentication_user)
# Запрос на получение данных о созданном пользователе PrivateUsersClient.get_user_api
actual_get_user_response_data = private_users_client.get_user_api(user_id=create_user_response.user.id)

# Для теста что работает validate_json_schema
# change = actual_get_user_response_data.json()
# change["user"]["email"] = 'test'
# print(change)

# Получаем JSON схему из модели ответа
expected_get_user_response_schema = GetUserResponseSchema.model_json_schema()
# Проверяем, что JSON ответ от API соответствует ожидаемой JSON схеме
validate_json_schema(
    instance=actual_get_user_response_data.json(),
    schema=expected_get_user_response_schema
)
