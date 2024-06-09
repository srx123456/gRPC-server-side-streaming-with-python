import json
import sys
import random
from json_operator import load_sorWeight,update_sorWeightRandom

def select_best_individuals(sorWeight, k=3):
    keys = list(sorWeight.keys())
    if len(keys) < k:
        raise ValueError("Not enough nodes to select from.")
    best_individuals = random.sample(keys, k)
    return best_individuals

# 示例主函数
def main():
    file_path = '../result/total2.txt'  # 修改为你的文件路径
    sorWeight = load_sorWeight(file_path)
    
    best_individuals = select_best_individuals(sorWeight, 4)
    print(best_individuals)
    
    update_sorWeightRandom(best_individuals,file_path)

if __name__ == "__main__":
    while(True):
        main()
