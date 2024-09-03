# import matplotlib.pyplot as plt

# # 数据
# # x = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# # y1 = [12, 15, 18, 20, 23, 26, 28, 31, 33]
# # y2 = [12, 11, 17, 18, 17, 21, 13, 20, 20]
# x = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# y1 = [10,12,14,16,18,20,22,24,26]
# y2 = [10,10,12,13,14,16,19,19,19]

# # 创建折线图
# plt.figure(figsize=(10, 6))  # 设置图形大小
# plt.plot(x, y1, marker='o', color='blue' , label='自适应选路机制')  # 第二行数据
# plt.plot(x, y2, marker='s', color='red' , label='随机选路机制')  # 第三行数据

# # 添加标题和标签
# # plt.title('从所有节点中选择3个节点')
# plt.title('从所有节点中选择4个节点')
# plt.xlabel('总节点数')
# plt.ylabel('到达阈值时迭代次数')
# plt.legend()  # 添加图例

# # 显示图形
# plt.show()

import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置中文字体
mpl.rcParams['font.family'] = 'SimSun'

# 数据
x = [4, 5, 6, 7, 8, 9, 10, 11, 12]
y1 = [12, 15, 18, 20, 23, 26, 28, 31, 33]
y2 = [12, 11, 17, 18, 17, 21, 13, 20, 20]

x2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]
y1_2 = [10, 12, 14, 16, 18, 20, 22, 24, 26]
y2_2 = [10, 10, 12, 13, 14, 16, 19, 19, 19]

# 创建折线图
plt.figure(figsize=(14, 6))  # 设置图形大小

# 第一个小图
plt.subplot(1, 2, 1)  # 创建第一个小图
plt.plot(x, y1, marker='o', color='blue', label='自适应选路机制')  # 第一组数据-折线1
plt.plot(x, y2, marker='s', color='red', label='随机选路机制')  # 第一组数据-折线2
plt.title('从所有节点中选择3个节点')  # 添加标题
plt.xlabel('总节点数')  # 添加横轴标签
plt.ylabel('到达阈值时迭代次数')  # 添加纵轴标签
plt.legend()  # 添加图例

# 第二个小图
plt.subplot(1, 2, 2)  # 创建第二个小图
plt.plot(x2, y1_2, marker='o', color='blue', label='自适应选路机制')  # 第二组数据-折线1
plt.plot(x2, y2_2, marker='s', color='red', label='随机选路机制')  # 第二组数据-折线2
plt.title('从所有节点中选择4个节点')  # 添加标题
plt.xlabel('总节点数')  # 添加横轴标签
plt.ylabel('到达阈值时迭代次数')  # 添加纵轴标签
plt.legend()  # 添加图例

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()

