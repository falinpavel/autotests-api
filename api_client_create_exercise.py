from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()
# Инициализируем запрос на создание пользователя
create_users_request = CreateUserRequestDict(
    email=get_random_email(),
    password="2556535",
    lastName="Ivanov",
    firstName="Ivan",
    middleName="Ivanovich",
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(request=create_users_request)
# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_users_request["email"],
    password=create_users_request["password"]
)
# Инициализируем клиент FilesClient
files_client = get_files_client(user=authentication_user)
# Инициализируем клиент CoursesClient
courses_client = get_courses_client(user=authentication_user)
# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(request=create_file_request)
print(f"Create file data: {create_file_response}")
# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Автоматизация тестирования API",
    maxScore=100,
    minScore=10,
    description="Автоматизация тестирования API с Python. Расширенный",
    estimatedTime="21 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(request=create_course_request)
print(f"Create course data: {create_course_response}")
# Инициализируем клиент ExercisesClient
files_client = get_exercises_client(user=authentication_user)
# Создаем упражнение в ранее созданный курс
create_exercise_request = CreateExerciseRequestDict(
    title="Основы работы с HTTPX",
    courseId=create_course_response["course"]["id"],
    maxScore=100,
    minScore=10,
    orderIndex=12,
    description="Практикуемся в использовании API клиентов",
    estimatedTime="2 weeks"
)
print(f"Create exercise data: {create_exercise_request}")
