from os import path

import hello_pb2
import hello_pb2_grpc

# 继承自hello_pb2_grpc.HelloServicer。
class Hello(hello_pb2_grpc.HelloServicer):

    # gRPC服务方法，用于处理客户端发起的请求。
    def Greet(self, request, context):
        file = ''
        file = request.name+", " + request.message
        print(file)
        # 使用yield语句返回一个hello_pb2.HelloResponse对象，其中的data属性被赋值为file。
        yield hello_pb2.HelloResponse(data=file.encode(encoding='utf-8'))