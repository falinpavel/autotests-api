import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FilesFixture
from fixtures.users import UserFixture, func_user


class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

    @property
    def id(self):
        return self.response.course.id

    @property
    def title(self):
        return self.request.title

    @property
    def description(self):
        return self.request.description

    @property
    def max_score(self):
        return self.request.max_score

    @property
    def min_score(self):
        return self.request.min_score

    @property
    def preview_file(self):
        return self.request.preview_file_id

    @property
    def estimated_time(self):
        return self.request.estimated_time

    @property
    def created_by_user(self):
        return self.request.created_by_user_id

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
        created_by_user=func_user.id
    )
    response = courses_client.create_course(request=requests)
    return CoursesFixture(request=requests, response=response)