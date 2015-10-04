
from sudokuproblem import SudokuProblem
from sudokugrid import SudokuGrid
from Aima import search



if __name__ == '__main__':
    g = SudokuGrid('48392.657967.458212518764935481.297672956413813.798245372689514814253769695417382')
    print(" --- INPUT ---")
    print(g)
    p = SudokuProblem(g)
    a = search.depth_first_tree_search(p)

    print("\n\n--- OUTPUT ---")
    print(a.state[0])