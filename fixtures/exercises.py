import pytest

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from fixtures.users import UserFixture, func_user


@pytest.fixture(scope="function")
def exercises_client(func_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(user=func_user.authentication_user)