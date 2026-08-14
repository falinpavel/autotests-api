# import pytest
#
#
# @pytest.fixture
# def create_user():
#     print("Precondition. Creating user")
#     user_data = {
#         "username": "test_user",
#         "email": "123@yandex.ru",
#         "dcb_bank_id": 123
#     }
#     yield user_data
#     print("Postcondition. Deleting user")
#
# def test_create_user(create_user):
#     assert create_user.get("username") == "test_user"
