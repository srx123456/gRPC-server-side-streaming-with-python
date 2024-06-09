import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

config = {}

with open('../data/totalPathFile.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        pairs = line.strip().split(',')
        key = pairs[0]
        value = pairs[1]
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

# 画图
# 节点聚集在一起的原因可能是因为使用了spring_layout布局算法，该算法会尽量使得连接的节点之间的距离最小化，从而导致节点聚集在一起。
# 如果你希望节点分散开来，可以尝试使用其他的布局算法，例如random_layout、circular_layout或shell_layout等。
# 这些布局算法可以使节点在图中均匀分布，从而避免节点聚集在一起。
pos = nx.circular_layout(G)  # 设置节点的布局
# pos = nx.random_layout(G)

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

nx.draw_networkx_edges(G, pos)
# nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')  # 设置节点的标签
# 绘制节点标签，调整位置
labels = nx.draw_networkx_labels(
    G, pos, font_size=8, font_color='black',
    bbox=dict(facecolor='white', edgecolor='none', alpha=0.9)  # 设置标签背景透明度
)

# 将标签移到节点图片的旁边
for node, t in labels.items():
    offset_x = 0.1  # 水平偏移量
    offset_y = -0.1  # 垂直偏移量
    pos[node][0] += offset_x
    pos[node][1] += offset_y
    t.set_position((pos[node][0], pos[node][1]))


plt.axis('off')  # 关闭坐标轴

plt.show()
