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

if __name__ == '__main__':
    instance = create_nqueens_problem_instance(8)

    set_initial_state(instance)

    print(instance.__dict__)