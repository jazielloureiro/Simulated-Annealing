from dataclasses import dataclass
from random import randint

@dataclass
class Item:
    weight: int
    value: int

@dataclass
class Knapsack:
    itens_amount: int
    itens: list[Item]
    solution: list[int]
    max_weight: int

def create_knapsack_problem_instance(itens_amount, max_knapsack_weight, min_item_weight, max_item_weight, min_item_value, max_item_value):
    instance = Knapsack(itens_amount, [], [], max_knapsack_weight)

    for _ in range(itens_amount):
        instance.itens += [Item(randint(min_item_weight, max_item_weight), randint(min_item_value, max_item_value))]

        instance.solution += [0]
    
    return instance

if __name__ == '__main__':
    instance = create_knapsack_problem_instance(20, 500, 1, 50, 1, 100)
    
    print(instance.__dict__)