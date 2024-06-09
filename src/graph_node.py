import networkx as nx
import matplotlib.pyplot as plt
import random

# 自动插入换行符的函数
def insert_line_breaks(label, max_length=10):
    return '\n'.join([label[i:i+max_length] for i in range(0, len(label), max_length)])

# 读取配置文件
config = {}

with open('../data/totalPathFile.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        pairs = line.strip().split(',')
        key = pairs[0]
        value = pairs[1]
        config[key] = value

# print(config)

# 创建图
G = nx.Graph()

# 添加边
for start, end in config.items():
    G.add_edge(start, end)

# 计算连通分量
connected_components = list(nx.connected_components(G))

# 生成随机颜色
colors = [plt.cm.rainbow(random.random()) for _ in range(len(connected_components))]

# 为每个连通分量分配颜色
node_colors = {}
for i, component in enumerate(connected_components):
    for node in component:
        node_colors[node] = colors[i]

# 画图
pos = nx.circular_layout(G)  # 设置节点的布局
# pos = nx.kamada_kawai_layout(G)

# 计算节点的度数
node_degrees = dict(G.degree())

# 绘制节点
node_collection = nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=[v * 50 for v in node_degrees.values()])

# 绘制边
# nx.draw_networkx_edges(G, pos)
# 绘制边，使用相同的颜色
for i, component in enumerate(connected_components):
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v in G.edges() if u in component and v in component], edge_color=colors[i], width=2)


# 绘制节点标签
# 绘制节点标签，自动换行
labels = {node: insert_line_breaks(node, max_length=8) for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_color='black', bbox=dict(facecolor='white', alpha=0.8))

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # 调整图像的边距

plt.axis('off')  # 关闭坐标轴

plt.show()
