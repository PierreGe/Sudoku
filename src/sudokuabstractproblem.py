from Aima import search
from sudokugrid import SudokuGrid
import copy


class SudokuAbstractProblem(search.Problem):
    def __init__(self, initial, grid):
        search.Problem.__init__(self, initial, None)
        self.grid = grid

    def actions(self, A):
        "The actions at a graph node are just its neighbors."
        grid, pos = A
        l = []
        for possibility in grid.possibleValue(pos):
            g = copy.deepcopy(grid)
            g.setOnGrid(pos, possibility)
            l.append([g, g.getFirstEmpty()])
        return l

    def result(self, state, action):
        "The result of going to a neighbor is just that neighbor."
        return action

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough."""
        if state[0] != None:
            return state[0].isFinished()
        return False


class SudokuSearchProblem(SudokuAbstractProblem):
    def __init__(self, grid):
        SudokuAbstractProblem.__init__(self, (grid, grid.getFirstEmpty()), grid)

    def actions(self, A):
        "The actions at a graph node are just its neighbors."
        grid, pos = A
        l = []
        for possibility in grid.possibleValue(pos):
            g = copy.deepcopy(grid)
            g.setOnGrid(pos, possibility)
            l.append([g, g.getFirstEmpty()])
        return l


class SudokuHeuristicProblem(SudokuAbstractProblem):
    def __init__(self, grid):
        SudokuAbstractProblem.__init__(self, (grid, grid.getBestEmpty()), grid)

    def actions(self, A):
        "The actions at a graph node are just its neighbors."
        grid, pos = A
        l = []
        for possibility in grid.possibleValue(pos):
            g = copy.deepcopy(grid)
            g.setOnGrid(pos, possibility)
            l.append([g, g.getBestEmpty()])
        return l

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        if state2[1] != None:  # grille pas rempli
            c = 10 - (len(state2[0].possibleValue(state2[1])))
        else:
            c = 0
        return c


if __name__ == '__main__':
    # g = SudokuGrid('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    # g = SudokuGrid('483921657967345821251876493548132976729564138136798245372689514814253769695417382')
    g = SudokuGrid('48392.657967.45821251876493548132976729564138136798245372689514814253769695417382')
    p = SudokuAbstractProblem(g)
    a = search.depth_first_tree_search(p)
    print(a.state[0])
