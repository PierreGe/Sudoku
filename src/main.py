
from sudokuproblem import SudokuSearchProblem, SudokuHeuristicProblem, SudokuHillClimbingProblem
from sudokugrid import SudokuGrid
from sudokusearch import numered_depth_first_tree_search, LimitReached, numered_best_first_tree_search, hill_climbing_global_max
from Aima import search



def main():

    print('Bonjour, voici vos choix: \n\n1- Comparer les 3 algos avec un sudoku tres simple\n2- Comparer les 3 algos avec un sudoku complexe\n3- Comparer les 3 algos avec une liste de 50 sudoku complexes')
    w = raw_input('Votre choix: ')

    if w == '1':
        f = ['...92..579.7.458212518764935481.297672956413813.798245372689514814253769.95417382']
    elif w == '2':
        f = ['003000600900305000001806400008102900700000008006708200002609500800003009005010300']
    elif w == '3':
        file100 = open("50sudoku.txt", 'r')
        f = file100.readlines()

    print('\n\nCombien d\'essais doivent faire les algos maximum?')
    limit = int(raw_input('Nombre d\'essais maximal: '))

    writeToFile = raw_input('\n\nEcrire les resultats dans un fichier .csv? (1 pour oui, n\'importe quoi sinon) : ')

    nomfichier = "result" + str(limit) + '.csv'
    resFile = open(nomfichier, 'w')
    resFile.write('limite de ' + str(limit) + '\n')
    result = ['Avec limite de ' + str(limit)]

    #seq = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    #seq = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..6..82....2..95..8..2.3..9..5.1.3..'

    a = 0

    for seq in f:
        a+=1

        print(" --- INPUT ---")
        g = SudokuGrid(seq)
        print(g)

        print("\n--- Hill climbing ---")
        g = SudokuGrid(seq)
        p = SudokuHillClimbingProblem(g)
        tentative = 1
        node = hill_climbing_global_max(p,tentative)
        hi = 1 if node.isFinished() else 0

        print(node)

        if node.isFinished():
            print("Succes !" + '\n\n')
        else:
            print("Echec malgre "+str(tentative)+ " test de configuration initiale differente")
            print("Ci dessus, un maximum local (" + str(node.getConflictNumber()) + " conflits restant)" + '\n\n')

        try:
            print("\n--- Heuristic ---")
            g = SudokuGrid(seq)
            p = SudokuHeuristicProblem(g)
            node, nbrNode = numered_best_first_tree_search(p, limit)

            print(node.state[0])
            print("Succes : Nombre de noeuds visites : " + str(nbrNode) + '\n\n')

            he = 1 if node.state[0].isFinished() else 0
        except LimitReached as e:
            print("ERROR : " + str(e) + '\n\n')
            he = 0

        try:
            print("\n--- Depth-First Search ---")
            g = SudokuGrid(seq)
            p = SudokuSearchProblem(g)
            node, nbrNode = numered_depth_first_tree_search(p, limit)

            print(node.state[0])
            print("Succes : Nombre de noeuds visites : " + str(nbrNode) + '\n\n')
            se = 1 if node.state[0].isFinished() else 0
        except LimitReached as e:
            print("ERROR : " + str(e) + '\n\n')
            se = 0

        result.append((hi, he, se))

        if writeToFile == '1':
            resFile.write(str(hi) + ',' + str(he) + ',' + str(se) + '\n')

        #Stop before the end of file with that:
        #if a==10: break






if __name__ == '__main__':
    main()