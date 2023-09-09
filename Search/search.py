# search.py
# ---------
# Licensing Information: You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC
# Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


class depthFirstSearchHelper:
    def __init__(self, cell):
        self.path = []
        self.cell = cell
class depthFirstSearchHelperCorner:
    def __init__(self, cell):
        self.path = []
        self.cell = cell[0]
        self.corners = cell[1]

def depthFirstSearch(problem):
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    stack = util.Stack()
    p = depthFirstSearchHelper(problem.getStartState())
    stack.push(p)
    visited = set()
    solution = []
    while not stack.isEmpty():
        p0 = stack.pop()
        if problem.isGoalState(p0.cell):
            solution = p0.path
            break
        visited.add(p0.cell)
        successors = problem.getSuccessors(p0.cell)
        for successor in successors:
            if successor[0] not in visited:
                #for i in stack.list:
                #    if i.cell == n[0]:
                #        break;
                #if(not any(x.cell == successor[0] for x in stack.list)):
                p1 = depthFirstSearchHelper(successor[0])
                p1.path = p0.path + [successor[1]]
                stack.push(p1)
    
    return solution

def breadthFirstSearch(problem):
    queue = util.Queue()
    if hasattr(problem, 'corners'):#unhashable type: 'list'  problem.corners
        p = depthFirstSearchHelperCorner(problem.getStartState())
        queue.push(p)
        visited = set()
        solution = []
        while not queue.isEmpty():
            p0 = queue.pop()
            if problem.isGoalState(p0.corners):
                solution = p0.path
                return solution
            if(p0.cell in visited):
                continue;
            visited.add((p0.cell,tuple( p0.corners)))
            #print(p0.cell)
            successors = problem.getSuccessors((p0.cell, p0.corners))
            for successor in successors:
                flag = True
                p1 = depthFirstSearchHelperCorner(successor[0])
                if not (p1.cell, tuple(p1.corners)) in visited:
                #if((p1.cell, p1.corners) not in visited and not any((x.cell, x.corners) == (p1.cell, p1.corners) for x in queue.list)):
                    p1.path = p0.path + [successor[1]]
                    queue.push(p1)
            #print(p1.cell,'a')
        return solution
    else:
        p = depthFirstSearchHelper(problem.getStartState())
        queue.push(p)
        #if(type(p.cell) == tuple):
        #    print("sd")
        visited = set()
        solution = []
        while not queue.isEmpty():
            p0 = queue.pop()
            if problem.isGoalState(p0.cell):
                solution = p0.path
                return solution
            visited.add(p0.cell)
            #print(p0.cell)
            successors = problem.getSuccessors(p0.cell)
            for successor in successors:
                if(successor[0] not in visited and not any(x.cell == successor[0] for x in queue.list)):
                    p1 = depthFirstSearchHelper(successor[0])
                    p1.path = p0.path + [successor[1]]
                    queue.push(p1)
        return solution

class uniformCostSearchHelper:
    def __init__(self, cell):
        self.path = []
        self.cell = cell
        self.cost = 0
class uniformCostSearchHelperCorner:
    def __init__(self, cell):
        self.path = []
        self.cell = cell[0]
        self.cost = 0
        self.corners = cell[1]

def uniformCostSearch(problem):
    p = uniformCostSearchHelper(problem.getStartState())
    priorityQueue = util.PriorityQueue()
    p.cost = 0
    priorityQueue.push(p, p.cost)
    visited = set()
    while not priorityQueue.isEmpty():
        p0 = priorityQueue.pop()
        if problem.isGoalState(p0.cell):
            return p0.path
        if p0.cell not in visited:
            visited.add(p0.cell)
            successors = problem.getSuccessors(p0.cell)
            for successor in successors:
               p1 = uniformCostSearchHelper(successor[0],)
               p1.path = p0.path + [successor[1]]
               p1.cost = p0.cost + successor[2]
               priorityQueue.push(p1, p1.cost)
               #print('---', p0.cell, "->", p1.cell, p1.cost)
    return []



def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    priorityQueue = util.PriorityQueue()
    if hasattr(problem, 'corners'):
        p = uniformCostSearchHelperCorner(problem.getStartState())
        p.cost = 0;
        priorityQueue.push(p,heuristic((p.cell,p.corners), problem) )
        visited = set()
        solution = []
        while not priorityQueue.isEmpty():
            p0 = priorityQueue.pop()
            if problem.isGoalState(p0.cell):
                solution = p0.path
                break;
            if (p0.cell,tuple(p0.corners)) not in visited:
                visited.add((p0.cell, tuple(p0.corners)))
                successors = problem.getSuccessors((p0.cell,p0.corners))
                for successor in successors:
                    p1 = uniformCostSearchHelperCorner(successor[0])
                    p1.path = p0.path + [successor[1]];
                    if (p1.cell,tuple(p1.corners)) not in visited and p1 not in priorityQueue.heap:
                        hhh = heuristic(successor[0], problem)
                        p1.cost = p0.cost + successor[2];
                        priorityQueue.push(p1, p1.cost + hhh )
        return solution
    else:
        p = uniformCostSearchHelper(problem.getStartState())
        p.cost = 0;
        priorityQueue.push(p,heuristic(p.cell, problem) )
        visited = set()
        solution = []
        while not priorityQueue.isEmpty():
            p0 = priorityQueue.pop()
            if problem.isGoalState(p0.cell):
                solution = p0.path
                break;
            if p0.cell not in visited:
                visited.add(p0.cell)
                successors = problem.getSuccessors(p0.cell)
                for successor in successors:
                    p1 = uniformCostSearchHelper(successor[0])
                    p1.path = p0.path + [successor[1]]
                    heurestic = heuristic(successor[0], problem)
                    p1.cost = p0.cost + successor[2];
                    priorityQueue.push(p1, p1.cost + heurestic )
        return solution


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
