from pydantic import BaseModel, Field
from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание структуры обьекта токена.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.

    ВАЖНО!!! Фейковые email и password можно использовать только в негативных сценариях,
    для позитивных сценариев необходимо передать в качестве этих аргументов реальные данные.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.

    ВАЖНО!!! Фейковый refresh_token можно использовать только в негативных сценариях,
    для позитивных сценариев необходимо передать в качестве аргумента реальный refresh_token.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.text)

class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос.
    """
    token: TokenSchema
