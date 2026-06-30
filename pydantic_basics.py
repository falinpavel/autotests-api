"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
import uuid

from pydantic import BaseModel, Field, computed_field, EmailStr, HttpUrl


class FileSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field(alias="userName")
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=0)
    description: str = "Default Course description"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")


default_course_model = CourseSchema(
    id="123",
    title="Default Course from model",
    maxScore=95,
    minScore=35,
    description="Default Course description",
    previewFile=FileSchema(
        id="file.id",
        filename="file.file-name",
        directory="file.directory",
        url="https://www.example.com"
    ),
    estimatedTime="default-preview-file-estimated-time",
    createdByUser=UserSchema(
        id="user.id",
        email="user@email.com",
        lastName="user.lastName",
        firstName="user.firstName",
        middleName="user.middleName"
    )
)
print(default_course_model)

default_course_model2 = CourseSchema(
    previewFile=FileSchema(
        filename="file.file-name2",
        directory="file.directory2",
        url="https://www.example.com"
    ),
    createdByUser=UserSchema(
        email="user@email2.com",
        lastName="user.lastName2",
        firstName="user.firstName2",
        middleName="user.middleName2"
    )
)
print(default_course_model2)

dict_course = {
    "id": "string3",
    "title": "string3",
    "maxScore": 30,
    "minScore": 10,
    "description": "string3",
    "previewFile": {
      "id": "string3",
      "filename": "string3",
      "directory": "string3",
      "url": "https://example.com/3"
    },
    "estimatedTime": "string3",
    "createdByUser": {
      "id": "string3",
      "email": "user3@example.com",
      "lastName": "string3",
      "firstName": "string3",
      "middleName": "string3"
    }
}
course_dict_model = CourseSchema(**dict_course)
print(course_dict_model)

json_course = """
{
    "id": "string3",
    "title": "string3",
    "maxScore": 30,
    "minScore": 10,
    "description": "string3",
    "previewFile": {
      "id": "string3",
      "filename": "string3",
      "directory": "string3",
      "url": "https://example.com/3"
    },
    "estimatedTime": "string3",
    "createdByUser": {
      "id": "string3",
      "email": "user3@example.com",
      "lastName": "string3",
      "firstName": "string3",
      "middleName": "string3"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(json_data=json_course)
print(course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))
