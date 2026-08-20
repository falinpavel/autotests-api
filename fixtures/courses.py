import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FilesFixture
from fixtures.users import UserFixture, func_user


class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture(scope="function")
def courses_client(func_user: UserFixture) -> CoursesClient:
    return get_courses_client(user=func_user.authentication_user)

@pytest.fixture(scope="function")
def func_courses(
        courses_client: CoursesClient,
        func_user: UserFixture,
        func_files: FilesFixture
) -> CoursesFixture:
    requests = CreateCourseRequestSchema(
        preview_file_id=func_files.response.file.id,
        created_by_user=func_user.response.user.id
    )
    response = courses_client.create_course(request=requests)
    return CoursesFixture(request=requests, response=response)