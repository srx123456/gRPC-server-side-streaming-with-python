import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

config = {}

with open('result/output.txt', 'r') as file:
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

# 创建节点图片字典
node_images = {}
for node in G.nodes:
    image_path = 'result/computer.jpeg'  # 替换为你的电脑图片路径
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
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')  # 设置节点的标签


plt.axis('off')  # 关闭坐标轴

plt.show()
