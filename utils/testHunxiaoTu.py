import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 新数据输入
data = np.array([
    ['sor1', 'sor4', 'sor2', 'sor6', 'sor2', 'sor1', 'sor1', 'sor2', 'sor6', 'sor2', 'sor1', 'sor1', 'sor2', 'sor6', 'sor5'],
    ['sor2', 'sor2', 'sor6', 'sor5', 'sor4', 'sor6', 'sor2', 'sor6', 'sor5', 'sor1', 'sor5', 'sor2', 'sor6', 'sor5', 'sor1'],
    ['sor4', 'sor5', 'sor4', 'sor1', 'sor5', 'sor4', 'sor4', 'sor4', 'sor1', 'sor5', 'sor6', 'sor4', 'sor5', 'sor1', 'sor4']
])

# 创建一个DataFrame，每一列代表一次结果
df = pd.DataFrame(data)

# 确定实验结果的顺序
ordered_sors = ['sor1', 'sor2', 'sor4', 'sor5', 'sor6']

# 创建一个映射，将每个sor映射为其在ordered_sors中的索引
value_to_int = {sor: idx for idx, sor in enumerate(ordered_sors)}

# 将DataFrame中的字符串数据转换为对应的整数
df_encoded = df.applymap(lambda x: value_to_int[x])

# 计算相关性矩阵
correlation_matrix = df_encoded.corr()

# 绘制相关性矩阵的热力图
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Results')
plt.show()

# 统计每列中与其它列相关性较低的蓝色色块数量
threshold = 0.5  # 设置相关性阈值
blue_blocks_counts = []

for col in correlation_matrix.columns:
    blue_blocks_count = np.sum(np.abs(correlation_matrix[col]) < threshold)
    blue_blocks_counts.append(blue_blocks_count)

# 打印结果
for idx, col in enumerate(correlation_matrix.columns):
    print(f"Number of blue blocks with correlation < {threshold} in column '{col}': {blue_blocks_counts[idx]}")
