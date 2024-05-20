from os import path
import subprocess
import json

import hello_pb2
import hello_pb2_grpc
import src.SorMsg

# 继承自hello_pb2_grpc.HelloServicer。
class Hello(hello_pb2_grpc.HelloServicer):
    def __init__(self):
        self.sorPathFile = "result/totalPathFile.txt"
        self.sorMsgFile = "result/totalMsgFile.txt"
        self.sorMsg= {}

    # gRPC真实的服务方法，用于处理客户端发起的请求。
    # 增加一种情况，客户端会同时上报 客户端的设备信息 以及 客户端的连接信息
    def Greet(self, request, context):
        file = ''
        
        # 传入的key是1.1.1.1
        if ':' not in request.name:
            parts = request.message.split(',')
            self.sorMsg[request.name] = src.SorMsg.SorMsg(cpu=parts[0], mem=parts[1], bw=parts[2]).__str__()
            # 打开文件，以重新写的方式写入
            with open(self.sorMsgFile, "w") as f:
                # 将字典转换为JSON格式的字符串，并写入文件
                f.write(json.dumps(self.sorMsg))
            return
        
        # 打开文件，以追加的方式写入
        with open(self.sorPathFile, "a") as f:
            f.write(request.name + "," + request.message + "\n")
        file = request.name+", " + request.message
        # 使用yield语句返回一个hello_pb2.HelloResponse对象，其中的data属性被赋值为file。
        yield hello_pb2.HelloResponse(data=file.encode(encoding='utf-8'))
        # 杀死其他的 src/graph.py 进程
        # subprocess.run(['pkill', '-f', 'src/graph.py'])
        subprocess.run(['pkill', '-f', 'python3 src/graph.py'])
        # 执行命令
        subprocess.Popen(['python3', 'src/graph.py'])


# # 打开一个文件用于读取
# with open('myfile.txt', 'r') as f:
#     # 从文件中读取JSON格式的字符串，并转换为字典
#     request_map = json.load(f)