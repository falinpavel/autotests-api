from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()
# Инициализируем запрос на создание пользователя
create_users_request = CreateUserRequestDict(
    email=get_random_email(),
    password="password",
    lastName="lastname",
    firstName="firstname",
    middleName="middlename",
)
# Отправляем POST запрос на создание пользователя
create_users_response = public_users_client.create_user(request=create_users_request)
print(f"Create user data: {create_users_response}")
# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_users_request["email"],
    password=create_users_request["password"]
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(user=authentication_user)
# Отправляем GET запрос на получение данных пользователя
get_users_response_data = private_users_client.get_user(user_id=create_users_response["user"]["id"])
print(f"Get user data: {get_users_response_data}")