from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()
# Инициализируем запрос на создание пользователя
create_users_request = CreateUserRequestDict(
    email=get_random_email(),
    password="password",
    lastName="lastname",
    firstName="firstname",
    middleName="middlename",
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
print(f"Created file data: {create_file_response}")
# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(request=create_course_request)
print(f"Create course data:{create_course_response}")
