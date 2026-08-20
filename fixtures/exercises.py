import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture, func_user


class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture(scope="function")
def exercises_client(func_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(user=func_user.authentication_user)

@pytest.fixture(scope="function")
def func_exercises(exercises_client: ExercisesClient, func_courses: CoursesFixture) -> ExercisesFixture:
    request = CreateExerciseRequestSchema(course_id=func_courses.response.course.id)
    response = exercises_client.create_exercise(request=request)
    return ExercisesFixture(request=request, response=response)