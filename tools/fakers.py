from faker import Faker
from faker.providers.person.ru_RU import Provider as RuProvider


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker
        self.faker.add_provider(RuProvider)

    def email(self) -> str:
        """
        Генерирует случайный email с доменом @gmail.com.

        :return: Случайный email.
        """
        return self.faker.email(domain="gmail.com")

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество.

        :return: Случайное отчество.
        """
        return self.faker.middle_name()

    def password(self) -> str:
        """
        Генерирует случайный пароль.

        :return: Случайный пароль.
        """
        return self.faker.password(
            length=250,
            special_chars=True,
            upper_case=True,
            lower_case=True
        )

    def text(self) -> str:
        """
        Генерирует случайный текст.

        :return: Случайный текст.
        """
        return self.faker.text(max_nb_chars=200)

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.

        :return: Случайное предложение.
        """
        return self.faker.sentence(nb_words=7, variable_nb_words=True)

    def min_score(self) -> int:
        """
        Генерирует случайный минимальный балл в диапазоне от 1 до 49.

        :return: Случайный балл.
        """
        return self.faker.random_int(min=1, max=49)

    def max_score(self) -> int:
        """
        Генерирует случайный максимальный балл в диапазоне от 50 до 100.

        :return: Случайный балл.
        """
        return self.faker.random_int(min=50, max=100)

    def random_integer(self, start: int = 1, end: int = 20) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(min=start, max=end)

    def estimated_time(self) -> str:
        """
        Генерирует строку с предполагаемым временем (например, "2 weeks").

        :return: Строка с предполагаемым временем.
        """
        return f"{self.random_integer(start=2, end=10)} weeks"

    def filename(self) -> str:
        """
        Генерирует случайное наименование файла.

        :return: Случайное наименование файла.
        """
        return self.faker.file_name()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4.

        :return: Случайный UUID4.
        """
        return self.faker.uuid4()

    def token(self):
        pass

# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker(locale="ru_RU"))