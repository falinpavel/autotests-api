from typing import TypedDict
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class UserDict(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponseDict(TypedDict):
    user: UserDict


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с приватными методами /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения данных о текущем пользователе.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по его идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод обновления пользователя по его идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с опциональными полями email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            url=f"/api/v1/users/{user_id}",
            json=request
        )

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по его идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id=user_id)
        return response.json()


# Добавляем builder для PrivateUsersClient
def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user=user))