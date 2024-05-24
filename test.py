import numpy as np
from deap import base, creator, tools, algorithms
import json
import random

class Individual(dict):
    pass

with open('result/totalMsgFile.txt', 'r') as f:
    # 从文件中读取JSON格式的字符串，并转换为字典
    sorMsg = json.load(f)

# 创建一个空的字典，用于存储数组的数据
sorWeight = {}

# 遍历字典的键值对
for key, value in sorMsg.items():
    # 将值分割并转换为浮点数，然后添加到列表中
    sorWeight[key] = [float(x.split(':')[1]) for x in value.split(',')]

# 定义优化问题
# 权重的大小只会影响带有权重的适应度值，但这个适应度值并不会被用于非支配排序。
creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))  # 多目标：最小化已使用的cpu和mem，最小化已使用的bw
creator.create("FitnessIndividual", Individual, fitness=creator.FitnessMulti)

# 定义评价函数
def evaluate(individual):
    values = list(individual.values())[0]
    cpu = values[0]
    mem = values[1]
    sent_bw = values[2]
    recv_bw = values[3]
    return cpu, mem, sent_bw, recv_bw

toolbox = base.Toolbox()

population = [creator.FitnessIndividual({key: value}) for key, value in sorWeight.items()]

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
for ind in best_individuals:
    # print(list(ind.keys())[0], list(ind.values())[0])
    print(list(ind.keys())[0])


