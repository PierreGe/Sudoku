from Aima import search


class SudokuGrid():
    def __init__(self,gridstr):
        assert len(gridstr) == 81
        self.grid = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = gridstr[i*9+j]

    def get(self,string):
        """
        :param string: par exemple "A9" avec A la ligne et 9 la colonne
        :return: la valeur dans le grid
        """
        assert len(string) ==2
        i = ord(string[0]) - ord("A")
        j = int(string[1])
        return grid[i][j]

    def __getitem__(self,i):
        return grid[i]

    def valueInSquare(self, i, j):
        pass

    def possibleValue(self):
        values = [[[i for i in range(1,10)] for j in range(9)] for k in range(9)]
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if j != k and self.grid[i][k] != 0 :
                        try:
                            values[i][j].remove(self.grid[i][k])
                        except:
                            pass
                    if i != k and self.grid[k][j] != 0:
                        try:
                            values[i][j].remove(self.grid[k][j])
                        except:
                            pass
        return values

    def assignANewValue(self):
        values = self.possibleValue()
        for i in range(9):
            for j in range(9):
                if values[i][j]:
                    return values[i][j][0]
        return False

    def isFull(self, other):
         pass

    def successor(self):
        self.assignANewValue()

    def goalReached(self):
        self.assignANewValue()

    @staticmethod
    def getFull():
        pass

    def __str__(self):
        string = ""
        for i in range(len(grid)):
            for j in range(len(i)):
                string += self.grid[i][j]
            string += "\n"




class SudokuSearchProblem(search.Problem):
    def __init__(self, initial, goal=None):
        search.Problem.__init__(self,initial,goal)
        pass

    def successor(self, state):
        """Given a state, return a sequence of (action, state) pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once. Iterators will work fine within the framework."""
        yield state.successor()

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Implement this
        method if checking against a single self.goal is not enough."""
        return state.goalReached()

    def value(self):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        pass #abstract



if __name__ == '__main__':

    g = SudokuGrid("200060000007004086000001300000000040090000000480000710900078000000050002020600501")
    p = SudokuSearchProblem(g,SudokuGrid.getFull())
    search.depth_first_tree_search(p)