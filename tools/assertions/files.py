import httpx
from pydantic import HttpUrl

from clients.errors_schema import (
    ValidationErrorResponseSchema,
    ValidationErrorSchema,
    InternalErrorResponseSchema
)
from clients.files.files_schema import (
    FileSchema,
    CreateFileRequestSchema,
    CreateFileResponseSchema,
    GetFileResponseSchema
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


def assert_files(actual: FileSchema, expected: FileSchema) -> None:
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.filename, expected=expected.filename, name="filename")
    assert_equal(actual=actual.directory, expected=expected.directory, name="directory")
    assert_equal(actual=actual.url, expected=expected.url, name="url")

def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema) -> None:
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # http://localhost:8000/static/test/340eb36c-075e-44c0-8c28-0925ea472eb0.png
    expected_file_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(actual=str(response.file.url), expected=expected_file_url, name="url")
    assert_equal(actual=response.file.filename, expected=request.filename, name="filename")
    assert_equal(actual=response.file.directory, expected=request.directory, name="directory")

def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
) -> None:
    assert_files(actual=get_file_response.file, expected=create_file_response.file)

def assert_file_is_accessible(url: HttpUrl | str) -> None:
    """
    Проверяет, что файл доступен по указанному URL.

    :param url: Ссылка на файл.
    :raises AssertionError: Если файл не доступен.
    """
    response = httpx.get(str(url))
    assert response.status_code == 200, f"Файл недоступен по URL: {url}"

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema) -> None:
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "filename"]  # Ошибка возникает в теле запроса, поле "filename".
            )
        ]
    )
    assert_validation_error_response(actual=actual, expected=expected)

def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema) -> None:
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустая директория.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "directory"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual=actual, expected=expected)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    # Ожидаемое сообщение об ошибке, если файл не найден
    expected = InternalErrorResponseSchema(details="File not found")
    # Используем ранее созданную функцию для проверки внутренней ошибки
    assert_internal_error_response(actual=actual, expected=expected)