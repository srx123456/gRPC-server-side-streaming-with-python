from __future__ import print_function
import logging
import time
import grpc
import random
import sys

from io import BytesIO, open

import hello_pb2
import hello_pb2_grpc

from src.LocalRemoteMapper import LocalRemoteMapper

messages = []

def createMapper():
    for _ in range(4):
        local = f"192.168.2.{random.randint(0, 255)}:{random.randint(0, 9999)}"
        remote = f"10.{random.randint(0, 254)}.10.123:{random.randint(0, 999)}"
        mapper = LocalRemoteMapper(local, remote)
        messages.append(mapper)
    return messages

# 通过gRPC与服务器建立连接，并发送带有姓名和消息的请求。
def greet_with_message(stub, name, message):
    start_time = time.time()
    # 使用stub.Greet方法发送一个HelloRequest请求，请求中包含了name和message。
    response = stub.Greet(hello_pb2.HelloRequest(name=name, message=message))
    elapsed_time = (time.time() - start_time) * 1000
    print(response, f'in {elapsed_time}secs')
    byte = [r for r in response][0].data

# 作用是与gRPC服务器建立连接
def run():
    # 创建一个与gRPC服务器的连接，服务器地址为localhost:50051。
    with grpc.insecure_channel('localhost:50051') as channel:
        # 创建一个HelloStub对象，该对象用于调用gRPC服务器上的方法。
        stub = hello_pb2_grpc.HelloStub(channel)
        # # 将要搜集的源和目的地址设置为一个类
        # messages_ = createMapper()

        # # 每个消息调用greet_with_message函数发送给服务器。
        # for message in messages_:
        #     greet_with_message(stub, name=message.local, message=message.remote)

        # 从命令行接收local和remote参数
        if len(sys.argv) != 3:
            print("请提供两个参数")
            sys.exit(1)

        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        greet_with_message(stub, name=arg1, message=arg2)

if __name__ == '__main__':
    logging.basicConfig()
    run()
