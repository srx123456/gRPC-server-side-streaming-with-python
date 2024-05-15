from concurrent import futures
import logging

import grpc

import hello_pb2
import hello_pb2_grpc

from src.hello import Hello

def serve():
    print('starting server..')
    # 创建一个 grpc.server 对象，并使用 futures.ThreadPoolExecutor(max_workers=10) 作为参数，指定服务器的最大工作线程数为 10。
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 将 Hello() 类的实例添加到服务器中。这个函数的作用是将 Hello() 类中定义的服务添加到服务器中，以便客户端可以调用。
    hello_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
    # 将服务器绑定到本地的 50051 端口上。这里使用的是不安全的端口，因为没有启用 SSL/TLS 加密。
    server.add_insecure_port('[::]:50051')
    print('started server on http://localhost:50051')
    # 开始接受客户端的请求并处理。
    server.start()
    server.wait_for_termination()


