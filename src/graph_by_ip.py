import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random

# 自动插入换行符的函数
def insert_line_breaks(label, max_length=10):
    return '\n'.join([label[i:i+max_length] for i in range(0, len(label), max_length)])

# 从节点名称中提取 IP 地址
def extract_ip(address):
    return address.split(':')[0]

# 读取配置文件
config = {}
with open('../data/totalPathFile.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        pairs = line.strip().split(',')
        key = extract_ip(pairs[0])
        value = extract_ip(pairs[1])
        config[key] = value

print(config)

G = nx.Graph()

# 添加边
for start, end in config.items():
    if start not in G.nodes:
        G.add_node(start)
    if end not in G.nodes:
        G.add_node(end)
    if not G.has_edge(start, end):
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

# 创建节点图片字典
node_images = {}
for node in G.nodes:
    image_path = '../data/computer.jpeg'  # 替换为你的电脑图片路径
    image = plt.imread(image_path)
    node_images[node] = image

# 计算节点的度数
node_degrees = dict(G.degree())

# 绘制节点
node_collection = nx.draw_networkx_nodes(G, pos, node_color='white', node_size=[v * 10 for v in node_degrees.values()])

# 设置节点图片
for node, image in node_images.items():
    ab = AnnotationBbox(OffsetImage(image, zoom=0.15), pos[node], frameon=False)
    plt.gca().add_artist(ab)

# 绘制边，使用相同的颜色
for i, component in enumerate(connected_components):
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v in G.edges() if u in component and v in component], edge_color=colors[i], width=2)

# 绘制节点标签，调整位置
labels = nx.draw_networkx_labels(G, pos, font_size=8, font_color='black', bbox=dict(facecolor='white', edgecolor='none', alpha=0.9))

# 将标签移到节点图片的外侧
label_offset = 0.13
for node, t in labels.items():
    x, y = pos[node]
    offset_x = label_offset if x < 0 else -label_offset  # 根据节点位置调整偏移方向
    offset_y = label_offset if y < 0 else -label_offset  # 根据节点位置调整偏移方向
    t.set_position((x + offset_x, y + offset_y))

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # 调整图像的边距

plt.axis('off')  # 关闭坐标轴

plt.show()
