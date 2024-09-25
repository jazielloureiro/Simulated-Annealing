from dataclasses import dataclass
import math
import random

@dataclass
class NQueens:
    queens_amount: int
    solution: list[int]

def create_nqueens_problem_instance(queens_amount):
    return NQueens(queens_amount, [0 for _ in range(queens_amount)])

def set_initial_state(instance):
    for i in range(instance.queens_amount):
        instance.solution[i] = random.randrange(instance.queens_amount)

def objective(instance, state):
    line_positions = [0 for _ in range(instance.queens_amount)]
    principal_diagonal_positions = [0 for _ in range(instance.queens_amount * 2 - 1)]
    secondary_diagonal_positions = [0 for _ in range(instance.queens_amount * 2 - 1)]
    conflicts = 0

    for i in range(instance.queens_amount):
        conflicts += line_positions[state[i]]
        line_positions[state[i]] += 1

        conflicts += principal_diagonal_positions[i + state[i]]
        principal_diagonal_positions[i + state[i]] += 1

        conflicts += secondary_diagonal_positions[instance.queens_amount - 1 - i + state[i]]
        secondary_diagonal_positions[instance.queens_amount - 1 - i + state[i]] += 1

    return conflicts

def get_random_neighbour_state(state):
    neighbour_state = state[:]
    item_index = random.randrange(len(neighbour_state))
    old_indexed_value = neighbour_state[item_index]

    while neighbour_state[item_index] == old_indexed_value:
        neighbour_state[item_index] = random.randrange(len(neighbour_state))

    return neighbour_state

def get_initial_temperature(instance, state):
    mean = 0

    for _ in range(1000):
        state = get_random_neighbour_state(state)

        objective_value = objective(instance, state)

        mean += objective_value / 1000 if objective_value > 0 else 0
    
    return mean * math.log(30)

def simulated_annealing(instance):
    temperature, old_temperature, iteration_state = 0, 0, instance.solution

    temperature = get_initial_temperature(instance, instance.solution)

    while temperature != old_temperature:
        for _ in range(100):
            neighbour_state = get_random_neighbour_state(iteration_state)
            objective_difference = objective(instance, neighbour_state) - objective(instance, iteration_state)

            if objective_difference < 0:
                iteration_state = neighbour_state

                if objective(instance, neighbour_state) < objective(instance, instance.solution):
                    instance.solution = iteration_state
            elif random.uniform(0, 1) < math.exp(-objective_difference / temperature):
                iteration_state = neighbour_state
        
        old_temperature = temperature
        temperature *= 0.95

if __name__ == '__main__':
    instance = create_nqueens_problem_instance(8)

    set_initial_state(instance)
    simulated_annealing(instance)

    print(instance.__dict__)