
from sudokuproblem import SudokuSearchProblem, SudokuHeuristicProblem, SudokuHillClimbingProblem
from sudokugrid import SudokuGrid
from sudokusearch import numered_depth_first_tree_search, LimitReached, numered_best_first_tree_search, hill_climbing_global_max
from Aima import search



def main():
    #seq = '...92..579.7.458212518764935481.297672956413813.798245372689514814253769.95417382'
    #seq = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    #seq = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..6..82....2..95..8..2.3..9..5.1.3..'
    seq = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    print(" --- INPUT ---")
    g = SudokuGrid(seq)
    print(g)
    p = SudokuSearchProblem(g)


    print("Hill climbing")
    g = SudokuGrid(seq)
    p = SudokuHillClimbingProblem(g)
    tentative = 20
    node = hill_climbing_global_max(p,tentative)
    print(node)
    if node.isFinished():
        print("Succes !")
    else:
        print("Echec malgre "+str(tentative)+ " test de configuration initiale differente")
        print("Ci dessus, un maximum local (" + str(node.getConflictNumber()) + " conflits restant)")


    try:
        print("Heuristic")
        g = SudokuGrid(seq)
        p = SudokuHeuristicProblem(g)
        node, nbrNode = numered_best_first_tree_search(p, 10000)
        print("\n\n--- OUTPUT ---")
        print(node.state[0])
        print("Succes : Nombre de noeuds visites : " + str(nbrNode))
    except LimitReached as e:
        print("ERROR : " + str(e))

    try:
        print("Search")
        g = SudokuGrid(seq)
        p = SudokuSearchProblem(g)
        node, nbrNode = numered_depth_first_tree_search(p, 10000)
        print("\n\n--- OUTPUT ---")
        print(node.state[0])
        print("Nombre de noeuds visites : " + str(nbrNode))
    except LimitReached as e:
        print("ERROR : " + str(e))







if __name__ == '__main__':
    main()