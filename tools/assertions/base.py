from typing import Any, Sized



def assert_status_code(actual_status_code: int, expected_status_code: int) -> None:
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual_status_code: Фактический статус-код ответа.
    :param expected_status_code: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual_status_code == expected_status_code, (
        f"Incorrect status code. "
        f"Actual status code: {actual_status_code} "
        f"Expected status code: {expected_status_code}"
    )

def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, (
        f"Incorrect value in: {name}. "
        f"Actual value: {actual} "
        f"Expected value: {expected}"
    )

def assert_is_true(actual: Any, name: str) -> None:
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(actual: Sized, expected: Sized, name: str) -> None:
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f'Expected length: {len(expected)}. '
        f'Actual length: {len(actual)}'
    )