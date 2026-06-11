import websockets
import asyncio


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket_connection:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket_connection.send(message)
        for _ in range(5):
            response = await websocket_connection.recv()
            print(response)


asyncio.run(client())
