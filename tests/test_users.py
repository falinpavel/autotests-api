from http import HTTPStatus
import pytest

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(json_data=response.text)

    assert_status_code(actual_status_code=response.status_code, expected_status_code=HTTPStatus.OK)
    assert_create_user_response(request=request, response=response_data)
    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
