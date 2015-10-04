from Aima import search
from Aima import csp



if __name__ == '__main__':

    #puzzle = csp.Sudoku('483921657967345821251876493548132976729564138136798245372689514814253769695417382') # solved (Figure 6.4.b)
    puzzle = csp.Sudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')

    puzzle.display(puzzle.infer_assignment())

    csp.AC3(puzzle)

    print
    if puzzle.goal_test(puzzle.infer_assignment()):
        print "Une solution a ete trouve:"
        puzzle.display(puzzle.infer_assignment())
    else:
        print "C'est un echec"
        puzzle.display(puzzle.infer_assignment())