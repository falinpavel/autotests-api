from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()
# Инициализируем запрос на создание пользователя
create_users_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="2556535",
    last_name="Ivanov",
    first_name="Ivan",
    middle_name="Ivanovich",
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(request=create_users_request)
# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_users_request.email,
    password=create_users_request.password
)
# Инициализируем клиент FilesClient
files_client = get_files_client(user=authentication_user)
# Инициализируем клиент CoursesClient
courses_client = get_courses_client(user=authentication_user)
# Загружаем файл
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(request=create_file_request)
print(f"Create file data: {create_file_response}")
# Создаем курс
create_course_request = CreateCourseRequestSchema(
    title="Автоматизация тестирования API",
    max_score=100,
    min_score=10,
    description="Автоматизация тестирования API с Python. Расширенный",
    estimated_time="21 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(request=create_course_request)
print(f"Create course data: {create_course_response}")
# Инициализируем клиент ExercisesClient
files_client = get_exercises_client(user=authentication_user)
# Создаем упражнение в ранее созданный курс
create_exercise_request = CreateExerciseRequestSchema(
    title="Основы работы с HTTPX",
    course_id=create_course_response.course.id,
    max_score=100,
    min_score=10,
    order_index=12,
    description="Практикуемся в использовании API клиентов",
    estimated_time="2 weeks"
)
print(f"Create exercise data: {create_exercise_request}")
