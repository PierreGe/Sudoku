from Aima import search
from Aima import csp



if __name__ == '__main__':

    puzzle = csp.Sudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    search.depth_first_tree_search(puzzle)

    print
    if puzzle.goal_test(puzzle.infer_assignment()):
        print "Une solution a été trouvé:"
        puzzle.display(puzzle.infer_assignment())
    else:
        print "C'est un échec" 
        puzzle.display(puzzle.infer_assignment())