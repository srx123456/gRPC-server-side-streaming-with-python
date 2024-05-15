from os import path
import subprocess

import hello_pb2
import hello_pb2_grpc

# 继承自hello_pb2_grpc.HelloServicer。
class Hello(hello_pb2_grpc.HelloServicer):
    def __init__(self):
        self.filename = "result/output.txt"

    # gRPC服务方法，用于处理客户端发起的请求。
    def Greet(self, request, context):
        file = ''
        
        # 打开文件，以追加的方式写入
        with open(self.filename, "a") as f:
            f.write(request.name + "," + request.message + "\n")
        file = request.name+", " + request.message
        print(file)
        # 使用yield语句返回一个hello_pb2.HelloResponse对象，其中的data属性被赋值为file。
        yield hello_pb2.HelloResponse(data=file.encode(encoding='utf-8'))
        # 杀死其他的 src/graph.py 进程
        # subprocess.run(['pkill', '-f', 'src/graph.py'])
        subprocess.run(['pkill', '-f', 'python3 src/graph.py'])
        # 执行命令
        subprocess.Popen(['python3', 'src/graph.py'])