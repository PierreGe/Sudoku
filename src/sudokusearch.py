

from Aima import search



class SudokuSearchProblem(search.Problem):
    def __init__(self, initial, goal=None):
        super(search.Problem, self).__init__(initial,goal)
        pass

    def successor(self, state):
        """Given a state, return a sequence of (action, state) pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once. Iterators will work fine within the framework."""
        pass #abstract

    def value(self):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        pass #abstract