from pydantic import BaseModel, Field, EmailStr, StringConstraints
from typing import Annotated

from tools.fakers import get_random_email


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание нового пользователя.
    """
    email: EmailStr = Field(default_factory=get_random_email)
    password: Annotated[str, StringConstraints(min_length=8, strip_whitespace=True)]
    last_name: str = Field(alias="lastName", default="Lucas", max_length=50, min_length=1)
    first_name: str = Field(alias="firstName", default="John", max_length=50, min_length=1)
    middle_name: str = Field(alias="middleName", default="Merideth", max_length=50, min_length=1)

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании пользователя.
    """
    user: UserSchema

