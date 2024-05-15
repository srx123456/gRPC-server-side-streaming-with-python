import networkx as nx
import matplotlib.pyplot as plt

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
nx.draw(G, with_labels=True)
plt.show()
