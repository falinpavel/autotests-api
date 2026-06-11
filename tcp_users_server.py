import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(10)

    server_socket.settimeout(1.0)

    print("Сервер запущен и ждет подключений...")

    # одна история сообщений для всех клиентов
    message_history = list()

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
            except socket.timeout:
                continue

            print(f"Пользователь с адресом: {client_address} подключился к серверу")

            data = client_socket.recv(1024).decode()

            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
            # добавляем новое сообщение в список
            message_history.append(data)

            response = '\n'.join(message_history)
            client_socket.send(response.encode())

            client_socket.close()

    except KeyboardInterrupt:
        print("Сервер остановлен")

    finally:
        server_socket.close()


if __name__ == "__main__":
    server()
