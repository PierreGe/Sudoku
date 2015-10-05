from Aima import search
from Aima import utils


class LimitReached(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


def numered_tree_search(problem, frontier, limit=10000):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Don't worry about repeated paths to a state. [Fig. 3.7]"""
    counter = 0
    frontier.append(search.Node(problem.initial))
    while frontier:
        node = frontier.pop()
        counter += 1
        if counter == limit:
            raise LimitReached("The limit number of node to be explored has been reached (" + str(limit) + ")")
        if problem.goal_test(node.state):
            return node, counter
        frontier.extend(node.expand(problem))
    return None, counter


def numered_depth_first_tree_search(problem, limit):
    "Search the deepest nodes in the search tree first."
    return numered_tree_search(problem, utils.Stack(), limit)


def numered_best_first_tree_search(problem, limit=10000, f=lambda node: node.path_cost):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    counter = 0
    f = utils.memoize(f, 'f')
    node = search.Node(problem.initial)
    if problem.goal_test(node.state):
        return node, counter
    frontier = utils.PriorityQueue(min, f)
    frontier.append(node)
    while frontier:
        node = frontier.pop()
        counter += 1
        if counter == limit:
            raise LimitReached("The limit number of node to be explored has been reached (" + str(limit) + ")")
        if problem.goal_test(node.state):
            return node, counter
        for child in node.expand(problem):
            if child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return node, counter
