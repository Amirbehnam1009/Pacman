from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best
        return legalMoves[chosenIndex]
    def evaluationFunction(self, currentGameState, action):
        #before
        #after
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        foodList = currentGameState.getFood().asList()

        if action == Directions.STOP:
            return float("-inf")

        for ghostState in newGhostStates:
            if (
                ghostState.getPosition() == newPos
                and ghostState.scaredTimer == 0
            ):
                return float("-inf")

        distance = []
        for food in foodList:
            distance.append(manhattanDistance(food, newPos))

        return -min(distance)
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.
    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.
    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.
    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
        val = self.getValue(gameState, 0, 0)
        return val[0]


    def getValue(self, gameState, index, depth): 
        if index >= gameState.getNumAgents():#0 1 2
            index = 0
            depth += 1

        if depth == self.depth:
            return self.evaluationFunction(gameState)

        if index == 0:
            return self.maxValue(gameState, index, depth)
        else:
            return self.minValue(gameState, index, depth)
        
    def minValue(self, gameState, index, depth):
        li = [];#('right', 2),('left', 4)
        allactions = gameState.getLegalActions(index)
        if len(allactions) == 0:
            return self.evaluationFunction(gameState)
        for action in allactions:
            if action == Directions.STOP:
                continue
            
            value = self.getValue(gameState.generateSuccessor(index, action), index + 1, depth)#1 : ('right',1)
            if type(value) is tuple:
                value = value[1] 

            li.append((action, value))
        return min(li, key = lambda x:x[1])

    def maxValue(self, gameState, index, depth):
        li = [];        
        allactions = gameState.getLegalActions(index)
        if len(allactions) == 0:
            return self.evaluationFunction(gameState)
        for action in gameState.getLegalActions(index):
            if action == Directions.STOP:
                continue
            
            value = self.getValue(gameState.generateSuccessor(index, action), index + 1, depth)
            if type(value) is tuple:
                value = value[1] 
            li.append((action, value))
        return max(li, key = lambda x:x[1])







class AlphaBetaAgent(MultiAgentSearchAgent):
 
    def getAction(self, gameState):
        alpha = -float("inf")
        beta = float("inf")
        val = self.getValue(gameState, 0, 0, alpha, beta)
        return val[0]

    def getValue(self, gameState, index, depth, alpha, beta): 
        if index >= gameState.getNumAgents():
            index = 0
            depth += 1

        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        if index == 0:
            return self.maxValue(gameState, index, depth, alpha, beta)
        else:
            return self.minValue(gameState, index, depth, alpha, beta)
        
    def minValue(self, gameState, index, depth, alpha, beta):
        last=(Directions.STOP,float("inf"));
        allactions = gameState.getLegalActions(index)
        if len(allactions) == 0:
            return self.evaluationFunction(gameState)
        for action in allactions:
            if action == Directions.STOP:
                continue
            
            value = self.getValue(gameState.generateSuccessor(index, action), index + 1, depth, alpha, beta)
            if type(value) is tuple:
                value = value[1] 
            if value <= last[1]:
                last = (action, value) 

            if last[1] < alpha:
                return last
            beta = min(beta, last[1])
        return last

    def maxValue(self, gameState, index, depth, alpha, beta):
        last=(Directions.STOP,-float("inf"));
        allactions = gameState.getLegalActions(index)
        if len(allactions) == 0:
            return self.evaluationFunction(gameState)
        for action in allactions:
            if action == Directions.STOP:
                continue
            
            value = self.getValue(gameState.generateSuccessor(index, action), index + 1, depth, alpha, beta)
            if type(value) is tuple:
                value = value[1] 
            if value >= last[1]:
                last = (action, value) 

            if last[1] >= beta:
                return last
            alpha = max(alpha, last[1])
        return last
 
class ExpectimaxAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):
        val = self.getValue(gameState, 0, 0)
        return val[0]

    def getValue(self, gameState, index, depth): 
        if index >= gameState.getNumAgents():
            index = 0
            depth += 1

        if depth == self.depth:
            return self.evaluationFunction(gameState)

        if index == 0:
            return self.maxValue(gameState, index, depth)
        else:
            return self.minValue(gameState, index, depth)
        
    def minValue(self, gameState, index, depth):

        last=(Directions.STOP,0);
        allactions = gameState.getLegalActions(index)
        if len(allactions) == 0:
            return self.evaluationFunction(gameState)
        e = 1.0/len(allactions)
        for action in allactions:
            if action == Directions.STOP:
                continue
            
            value = self.getValue(gameState.generateSuccessor(index, action), index + 1, depth)
            if type(value) is tuple:
                value = value[1] 
            last = tuple((action, last[1]+value+e))
        return last

    def maxValue(self, gameState, index, depth):
        li = [];
        last=(Directions.STOP,-float("inf"));
        allactions = gameState.getLegalActions(index)
        if len(allactions) == 0:
            return self.evaluationFunction(gameState)
        for action in allactions:
            if action == Directions.STOP:
                continue
            
            value = self.getValue(gameState.generateSuccessor(index, action), index + 1, depth)
            if type(value) is tuple:
                value = value[1] 
            li.append(value)
            if max(li) == value:
                last = (action, value) 
        return last

def betterEvaluationFunction(currentGameState):

 
    pos = currentGameState.getPacmanPosition()

    manhattean_ghost = [ manhattanDistance(x.getPosition(), pos) for x in currentGameState.getGhostStates()]
    manhattean_food = [ manhattanDistance(x, pos) for x in currentGameState.getFood().asList()]
    if len(manhattean_food) == 0:
        manhattean_food .append(1)

    s = -min(manhattean_food) +min(manhattean_ghost)/1000 +currentGameState.getScore() - 50*len(currentGameState.getCapsules())
    return  s
# Abbreviation
better = betterEvaluationFunction