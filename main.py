from dataclasses import dataclass
import math
import random

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
        instance.itens += [Item(random.randint(min_item_weight, max_item_weight), random.randint(min_item_value, max_item_value))]

        instance.solution += [0]
    
    return instance

def set_initial_state(instance, item_probability):
    for i in range(instance.itens_amount):
        if random.uniform(0, 1) <= (instance.itens_amount * item_probability) / instance.itens_amount:
            instance.solution[i] = 1

def objective(instance, state):
    total_weight, total_value_inserted, total_value = 0, 0, 0

    for i in range(instance.itens_amount):
        if state[i] == 1:
            total_value_inserted += instance.itens[i].value
            total_weight += instance.itens[i].weight
        
        total_value += instance.itens[i].value

    return total_value_inserted - total_value * max(0, total_weight - instance.max_weight)

def get_random_neighbour_state(instance):
    neighbour_state = instance.solution[:]
    item_index = random.randrange(instance.itens_amount)

    neighbour_state[item_index] = 1 - neighbour_state[item_index]

    return neighbour_state

def simulated_annealing(instance):
    temperature, old_temperature, iteration_state = 100, 0, instance.solution

    while temperature != old_temperature:
        for _ in range(100):
            neighbour_state = get_random_neighbour_state(instance)
            objective_difference = objective(instance, iteration_state) - objective(instance, neighbour_state)

            if objective_difference < 0:
                iteration_state = neighbour_state

                if objective(instance, neighbour_state) > objective(instance, instance.solution):
                    instance.solution = iteration_state
            elif random.uniform(0, 1) < math.exp(-objective_difference / temperature):
                iteration_state = neighbour_state
        
        old_temperature = temperature
        temperature *= 0.95

if __name__ == '__main__':
    instance = create_knapsack_problem_instance(100, 500, 1, 50, 1, 100)

    set_initial_state(instance, 0.1)
    simulated_annealing(instance)
    print(instance.__dict__)