import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# 源数据
data = [
    ['1.0.43.1', '1.0.44.1', '1.0.41.1', '1.0.53.1', '1.0.41.1', '1.0.43.1', '1.0.44.1', '1.0.41.1', '1.0.53.1', '1.0.41.1', '1.0.43.1', '1.0.44.1', '1.0.41.1', '1.0.53.1', '1.0.43.1'],
    ['1.0.41.1', '1.0.53.1', '1.0.45.1', '1.0.43.1', '1.0.45.1', '1.0.41.1', '1.0.53.1', '1.0.45.1', '1.0.43.1', '1.0.45.1', '1.0.41.1', '1.0.53.1', '1.0.45.1', '1.0.43.1', '1.0.41.1'],
    ['1.0.45.1', '1.0.43.1', '1.0.44.1', '1.0.44.1', '1.0.53.1', '1.0.45.1', '1.0.43.1', '1.0.44.1', '1.0.44.1', '1.0.53.1', '1.0.45.1', '1.0.43.1', '1.0.44.1', '1.0.44.1', '1.0.45.1']
]

# 转置数据，使每列成为一组
data = np.array(data).T

# 所有可能的标签
labels = sorted(set(data.flatten()))

# 生成混淆矩阵
y_true = data[:, 0]  # 第一列作为真实标签
y_pred = data[:, 1]  # 第二列作为预测标签

conf_matrix = confusion_matrix(y_true, y_pred, labels=labels)

# 绘制混淆矩阵
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()

tick_marks = np.arange(len(labels))
plt.xticks(tick_marks, labels, rotation=45)
plt.yticks(tick_marks, labels)

plt.xlabel('Predicted Label')
plt.ylabel('True Label')

# 在图上显示数值
thresh = conf_matrix.max() / 2.
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        plt.text(j, i, format(conf_matrix[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if conf_matrix[i, j] > thresh else "black")

plt.tight_layout()
plt.show()
