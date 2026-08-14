import pytest
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def first_name(self) -> str:
        return self.request.first_name

    @property
    def last_name(self) -> str:
        return self.request.last_name

    @property
    def middle_name(self) -> str:
        return self.request.middle_name

    @property
    def id(self) -> str:
        return self.response.user.id

@pytest.fixture(scope="function")
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture(scope="function")
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()

@pytest.fixture(scope="function")
def func_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request=request)
    return UserFixture(request=request, response=response)

@pytest.fixture(scope="session")
def session_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request=request)
    return UserFixture(request=request, response=response)