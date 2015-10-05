
from sudokuproblem import SudokuProblem
from sudokugrid import SudokuGrid
from sudokusearch import numered_depth_first_tree_search, LimitReached
from Aima import search



def main():
    #g = SudokuGrid('...92..579.7.458212518764935481.297672956413813.798245372689514814253769.95417382')
    #g = SudokuGrid('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    g = SudokuGrid('4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
    print(" --- INPUT ---")
    print(g)
    p = SudokuProblem(g)
    try:
        node, nbrNode = numered_depth_first_tree_search(p, 10000)
        print("\n\n--- OUTPUT ---")
        print(node.state[0])
        print("Nombre de noeuds visites : " + str(nbrNode))
    except LimitReached as e:
        print("ERROR : " + str(e))


if __name__ == '__main__':
    main()