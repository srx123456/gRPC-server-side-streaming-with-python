from deap import base, creator, tools, algorithms
import numpy as np
import random

# 定义优化问题
# 权重的大小只会影响带有权重的适应度值，但这个适应度值并不会被用于非支配排序。
creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))  # 多目标：最小化已使用的cpu和mem，最小化已使用的bw
creator.create("Individual", list, fitness=creator.FitnessMulti)

# 定义评价函数
def evaluate(individual):
    cpu = individual[0]
    mem = individual[1]
    sent_bw = individual[2]
    recv_bw = individual[3]
    return cpu, mem, sent_bw, recv_bw  # NSGA-II 默认是最小化目标

toolbox = base.Toolbox()

# # 以下是你的设备数据
# data = np.array([
#     [0.49049493, 0.65887901, 0.90775115],
#     [0.35043245, 0.16171948, 0.30046654],
#     [0.30115282, 0.78511499, 0.77051483],
#     [0.38966305, 0.44359973, 0.23062955],
#     [0.81362477, 0.20212014, 0.59442622]
# ])
n_samples = 10
n_features = 4
data = np.random.rand(n_samples, n_features)
print(data)

# 初始化种群
population = [creator.Individual(row) for row in data]

toolbox.register("evaluate", evaluate)  # 评价函数
toolbox.register("select", tools.selNSGA2)

# 计算种群中每个个体的适应度
fits = toolbox.map(toolbox.evaluate, population)
for fit, ind in zip(fits, population):
    ind.fitness.values = fit

# 运行遗传算法
population = toolbox.select(population, len(population))

# 使用帕累托排序对种群进行排序
sorted_pop = tools.sortNondominated(population, len(population))
print(sorted_pop)

# 输出最优解
best_individuals = tools.selBest(population, k=3)  # 选择得分最高的三个节点
print(best_individuals)

# 非支配排序遗传算法（NSGA-II）是一种多目标优化算法，它的学习资源主要包括研究论文、书籍和在线教程。

# 研究论文：NSGA-II的原始论文是" A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II"，由 Kalyanmoy Deb, Amrit Pratap, Sameer Agarwal 和 T. Meyarivan 在 2002 年发表。这篇论文详细介绍了 NSGA-II 的原理和实现。

# 书籍：多目标优化的经典书籍包括 Kalyanmoy Deb 的 "Multi-Objective Optimization Using Evolutionary Algorithms" 和 Carlos A. Coello Coello 的 "Evolutionary Algorithms for Solving Multi-Objective Problems"。这些书籍详细介绍了多目标优化和遗传算法，包括 NSGA-II。

# 在线教程：网上有许多关于 NSGA-II 的教程和实例，例如在 GitHub、Medium、Towards Data Science 等网站上，都可以找到相关的教程。

# 开源库：很多机器学习和优化的开源库，如 DEAP（Distributed Evolutionary Algorithms in Python），jMetal（Java库），都实现了 NSGA-II 算法，并提供了详细的文档和示例，可以通过阅读源代码和文档来学习 NSGA-II。

