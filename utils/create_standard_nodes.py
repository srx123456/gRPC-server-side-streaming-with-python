import json

# 初始化要生成的节点数量范围
node_counts = range(4, 100)

# 初始化每个节点的初始状态
initial_state = {
    "CPU": 0.1,
    "Mem": 0.1,
    "SendBw": 0.1,
    "RecvBw": 0.1
}

# 初始化节点字典
node_data = {}

# 循环生成不同数量的节点情况
for count in node_counts:
    # 生成不同数量的节点ip地址
    ips = [f"1.{i}.{j}.1" for i in range(0, 255) for j in range(0, 255)]
    # 初始化节点数据
    data = {ip: ",".join([f"{k}:{v}" for k, v in initial_state.items()]) for ip in ips}
    # 将节点数据添加到总的节点字典中
    node_data[count] = data

# 将节点数据保存为JSON文件
with open("../result/stardand.txt", "w") as f:
    json.dump(node_data, f, indent=4)
