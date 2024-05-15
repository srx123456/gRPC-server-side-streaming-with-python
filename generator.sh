#!/usr/bin/env bash
# 使用grpc_tools.protoc模块中的python3命令来生成gRPC代码的工具命令。
# -I 'protos'参数指定了protos目录作为导入路径，用于查找.proto文件。
# --python_out='.'参数指定生成的Python代码的输出目录为当前目录。
# --grpc_python_out='.'参数指定生成的gRPC Python代码的输出目录为当前目录。
# 'protos'/*.proto表示要编译的.proto文件的路径，这里使用通配符*匹配protos目录下的所有.proto文件。
python3 -m grpc_tools.protoc -I 'protos' \
    --python_out='.' \
    --grpc_python_out='.' 'protos'/*.proto
