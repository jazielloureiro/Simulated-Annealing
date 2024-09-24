from dataclasses import dataclass
from random import randint, uniform

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

def set_initial_state(instance, item_probability):
    for i in range(instance.itens_amount):
        if uniform(0, 1) <= (instance.itens_amount * item_probability) / instance.itens_amount:
            instance.solution[i] = 1

def objective(instance):
    total_weight, total_value_inserted, total_value = 0, 0, 0

    for i in range(instance.itens_amount):
        if instance.solution[i] == 1:
            total_value_inserted += instance.itens[i].value
            total_weight += instance.itens[i].weight
        
        total_value += instance.itens[i].value

    return total_value_inserted - total_value * max(0, total_weight - instance.max_weight)

if __name__ == '__main__':
    instance = create_knapsack_problem_instance(20, 500, 1, 50, 1, 100)

    set_initial_state(instance, 0.1)
    
    print(instance.__dict__)
    print(objective(instance))