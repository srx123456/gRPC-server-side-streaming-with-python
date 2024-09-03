import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib as mpl

# 设置中文字体
mpl.rcParams['font.family'] = 'SimSun'

# 读取数据
data = []
with open('../data/compare.csv', 'r') as file:
    for line in file:
        columns = line.strip().split(',')
        data.append([float(x) for x in columns])
        
# 提取数据
x = [row[0] for row in data]
y1 = [row[1] for row in data]
y2 = [row[2] for row in data]
y3 = [row[3] for row in data]

# 创建折线图
plt.figure(figsize=(10, 6))
plt.plot(x, y1, marker='o', color='blue', label='代理')  # 第二列数据
plt.plot(x, y2, marker='s', color='green', label='封包')  # 第三列数据
plt.plot(x, y3, marker='^', color='red', label='系统route')  # 第四列数据

# 添加标题和标签
plt.title('不同的实现下带宽与丢包比例关系')
plt.xlabel('带宽 (Mbps)')
plt.ylabel('丢包比例')

# 添加图例
plt.legend()

# 标出图例位置
plt.text(x[-1], y1[-1], '代理', verticalalignment='bottom', horizontalalignment='right', color='blue')
plt.text(x[-1], y2[-1], '封包', verticalalignment='bottom', horizontalalignment='right', color='green')
plt.text(x[-1], y3[-1], '系统route', verticalalignment='bottom', horizontalalignment='right', color='red')

# 显示图形
plt.show()
