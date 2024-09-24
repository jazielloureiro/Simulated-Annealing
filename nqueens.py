from dataclasses import dataclass
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

if __name__ == '__main__':
    instance = create_nqueens_problem_instance(8)

    set_initial_state(instance)

    print(instance.__dict__)
    print(objective(instance, instance.solution))
    print(get_random_neighbour_state(instance.solution))