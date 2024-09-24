from dataclasses import dataclass

@dataclass
class NQueens:
    queens_amount: int
    solution: list[int]

def create_nqueens_problem_instance(queens_amount):
    instance = NQueens(queens_amount, [0 for _ in range(queens_amount)])
    
    return instance

if __name__ == '__main__':
    instance = create_nqueens_problem_instance(8)