import grpc

import user_service_pb2_grpc
import user_service_pb2


channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

responses = stub.GetUser(user_service_pb2.GetUserRequest(username="John"))
print(responses)