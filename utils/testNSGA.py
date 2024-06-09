import numpy as np
from deap import base, creator, tools, algorithms
import json
import random
import math

from json_operator import load_sorWeight,update_sorWeight

# Constants
P_MIN = 0.2
P_MAX = 0.7
GAMMA = 0.05  # Choose a value for γ (you can adjust it based on your needs)
MAX_BW = 100  # Maximum bandwidth in Mbps (example value)

class Individual(dict):
    pass

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

def main():
    global sorWeight
    sorWeight = load_sorWeight('../data/total1.txt')

    creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))
    creator.create("FitnessIndividual", Individual, fitness=creator.FitnessMulti)

    toolbox = base.Toolbox()
    population = [creator.FitnessIndividual({key: value}) for key, value in sorWeight.items()]
    toolbox.register("evaluate", evaluate)
    toolbox.register("select", tools.selNSGA2)
    toolbox.register("mate", custom_mate)
    toolbox.register("mutate", custom_mutate)

    # Calculate initial fitness
    fits = toolbox.map(toolbox.evaluate, population)
    for fit, ind in zip(fits, population):
        ind.fitness.values = fit

    generation = 0
    max_generations = 100

    while generation < max_generations:
        CXPB = P_MIN + (P_MAX - P_MIN) * (1 - math.exp(-generation))
        MUTPB = P_MIN + (P_MAX - P_MIN) * (1 - math.exp(-GAMMA * generation))

        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fits = toolbox.map(toolbox.evaluate, invalid_ind)
        for fit, ind in zip(fits, invalid_ind):
            ind.fitness.values = fit

        population[:] = offspring
        generation += 1

    sorted_pop = tools.sortNondominated(population, len(population), first_front_only=True)

    best_individuals = tools.selBest(population, k=4)
    for ind in best_individuals:
        print(list(ind.keys())[0])
    update_sorWeight(best_individuals,'../data/total1.txt')

if __name__ == "__main__":
    while(True):
        main()
