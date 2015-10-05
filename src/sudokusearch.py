
from Aima import search
from Aima import utils


class LimitReached(Exception):
    def __init__(self):
        pass

def numered_tree_search(problem, frontier, limit):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Don't worry about repeated paths to a state. [Fig. 3.7]"""
    counter = 0
    frontier.append(search.Node(problem.initial))
    while frontier:
        node = frontier.pop()
        counter += 1
        if counter == limit:
            raise LimitReached
        if problem.goal_test(node.state):
            return node,counter
        frontier.extend(node.expand(problem))
    return None, counter

def numered_depth_first_tree_search(problem, limit):
    "Search the deepest nodes in the search tree first."
    return numered_tree_search(problem, utils.Stack(), limit)