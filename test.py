import numpy as np
from deap import base, creator, tools, algorithms
import json
import random
import math

# Constants
P_MIN = 0.2
P_MAX = 0.7
GAMMA = 0.05 
MAX_BW = 100  

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
    # Constraints
    if cpu > 0.85 or mem > 0.8 or sent_bw > MAX_BW * 0.8 or recv_bw > MAX_BW * 0.8:
        return 1e6, 1e6, 1e6, 1e6  # Assign a high fitness value if constraints are not met
    return cpu, mem, sent_bw, recv_bw

toolbox = base.Toolbox()

population = [creator.FitnessIndividual({key: value}) for key, value in sorWeight.items()]

toolbox.register("evaluate", evaluate)  # 评价函数
toolbox.register("select", tools.selNSGA2)
# Custom mate and mutate functions to handle dictionary-based individuals
def custom_mate(ind1, ind2):
    keys1 = list(ind1.keys())
    keys2 = list(ind2.keys())
    if len(keys1) > 1 and len(keys2) > 1:
        cxpoint1 = random.randint(1, len(keys1) - 1)
        cxpoint2 = random.randint(1, len(keys2) - 1)
        temp = keys1[cxpoint1:]
        keys1[cxpoint1:] = keys2[cxpoint2:]
        keys2[cxpoint2:] = temp
        new_ind1 = {key: ind1[key] for key in keys1}
        new_ind2 = {key: ind2[key] for key in keys2}
        ind1.clear()
        ind1.update(new_ind1)
        ind2.clear()
        ind2.update(new_ind2)

def custom_mutate(ind):
    keys = list(ind.keys())
    if len(keys) > 1:
        mut_point = random.randint(0, len(keys) - 1)
        new_key = random.choice(list(sorWeight.keys()))
        ind[keys[mut_point]] = sorWeight[new_key]

toolbox.register("mate", custom_mate)
toolbox.register("mutate", custom_mutate)

# 计算种群中每个个体的适应度
fits = toolbox.map(toolbox.evaluate, population)
for fit, ind in zip(fits, population):
    ind.fitness.values = fit

# Initialize parameters
generation = 0
max_generations = 100

# Evolution loop
while generation < max_generations:
    # Update crossover and mutation probabilities
    CXPB = P_MIN + (P_MAX - P_MIN) * (1 - math.exp(-generation))
    MUTPB = P_MIN + (P_MAX - P_MIN) * (1 - math.exp(-GAMMA * generation))

    # Select the next generation
    offspring = toolbox.select(population, len(population))
    offspring = list(map(toolbox.clone, offspring))

    # Apply crossover and mutation on the offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < MUTPB:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fits = toolbox.map(toolbox.evaluate, invalid_ind)
    for fit, ind in zip(fits, invalid_ind):
        ind.fitness.values = fit

    # Replace the current population with the offspring
    population[:] = offspring

    # Increment the generation counter
    generation += 1


# 使用帕累托排序对种群进行排序
sorted_pop = tools.sortNondominated(population, len(population))
print(sorted_pop)

# 输出最优解
best_individuals = tools.selBest(population, k=3)  # 选择得分最高的三个节点
for ind in best_individuals:
    # print(list(ind.keys())[0], list(ind.values())[0])
    print(list(ind.keys())[0])