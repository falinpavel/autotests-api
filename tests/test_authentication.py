from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
def test_login():
    public_users_client = get_public_users_client()
    request_create_user = CreateUserRequestSchema()
    response_create_user = public_users_client.create_user(request=request_create_user)

    authentication_client = get_authentication_client()
    request_authentication = LoginRequestSchema(email=response_create_user.user.email, password=request_create_user.password)
    response_login = authentication_client.login_api(request=request_authentication)
    response_login_data = LoginResponseSchema.model_validate_json(json_data=response_login.text)

    assert_status_code(actual_status_code=response_login.status_code, expected_status_code=HTTPStatus.OK)
    assert_login_response(response=response_login_data)
    validate_json_schema(instance=response_login.json(), schema=response_login_data.model_json_schema())
