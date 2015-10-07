
from sudokuproblem import SudokuSearchProblem, SudokuHeuristicProblem, SudokuHillClimbingProblem
from sudokugrid import SudokuGrid
from sudokusearch import numered_depth_first_tree_search, LimitReached, numered_best_first_tree_search, hill_climbing_global_max
from Aima import search



def main():
    f = ['...92..579.7.458212518764935481.297672956413813.798245372689514814253769.95417382']
    seq = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    #seq = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..6..82....2..95..8..2.3..9..5.1.3..'
    #f = ['003000600900305000001806400008102900700000008006708200002609500800003009005010300']

    limit = 1000

    file100 = open("100sudoku.txt", 'r')
    resFile = open('result1000.csv', 'w')
    resFile.write('limite de ' + str(limit) + '\n')

    #f = file100.readlines()
    result = ['Avec limite de ' + str(limit)]
    a = 0

    for seq in f:
        a+=1

        print(" --- INPUT ---")
        g = SudokuGrid(seq)
        print(g)

        print("Hill climbing")
        g = SudokuGrid(seq)
        p = SudokuHillClimbingProblem(g)
        tentative = 0
        node = hill_climbing_global_max(p,tentative)
        print(node)
        hi = node.isFinished()
        if node.isFinished():
            print("Succes !")
        else:
            print("Echec malgre "+str(tentative)+ " test de configuration initiale differente")
            print("Ci dessus, un maximum local (" + str(node.getConflictNumber()) + " conflits restant)")


        try:
            print("Heuristic")
            g = SudokuGrid(seq)
            p = SudokuHeuristicProblem(g)
            node, nbrNode = numered_best_first_tree_search(p, limit)
            print("\n\n--- OUTPUT ---")
            print(node.state[0])
            print("Succes : Nombre de noeuds visites : " + str(nbrNode))
            he = nbrNode if node.state[0].isFinished() else False
        except LimitReached as e:
            print("ERROR : " + str(e))
            he = False

        try:
            print("Search")
            g = SudokuGrid(seq)
            p = SudokuSearchProblem(g)
            node, nbrNode = numered_depth_first_tree_search(p, limit)
            print("\n\n--- OUTPUT ---")
            print(node.state[0])
            print("Nombre de noeuds visites : " + str(nbrNode))
            se = nbrNode if node.state[0].isFinished() else False
        except LimitReached as e:
            print("ERROR : " + str(e))
            se = False

        result.append((hi, he, se))
        print('Sudoku #' + str(a))
        print result[-1]

        resFile.write(str(hi) + ',' + str(he) + ',' + str(se) + '\n')

        #Stop before the end of file with that:
        #if a==10: break






if __name__ == '__main__':
    main()