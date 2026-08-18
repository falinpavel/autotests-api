from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
def test_login(func_user: UserFixture, authentication_client: AuthenticationClient):
    request = LoginRequestSchema(email=func_user.email, password=func_user.password)
    response = authentication_client.login_api(request=request)
    response_data = LoginResponseSchema.model_validate_json(json_data=response.text)

    assert_status_code(actual_status_code=response.status_code, expected_status_code=HTTPStatus.OK)
    assert_login_response(response=response_data)
    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
