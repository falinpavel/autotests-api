from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default=f"{fake.uuid4()}.png")
    directory: str = Field(default = "test")
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос создания файла.
    """
    file: FileSchema