# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent
import collections


class ValueIterationAgent(ValueEstimationAgent):
    """
    * Please read learningAgents.py before reading this.*

    A ValueIterationAgent takes a Markov decision process
    (see mdp.py) on initialization and runs value iteration
    for a given number of iterations using the supplied
    discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
        Your value iteration agent should take an mdp on
        construction, run the indicated number of iterations
        and then act according to the resulting policy.

        Some useful mdp methods you will use:
            mdp.getStates()
            mdp.getPossibleActions(state)
            mdp.getTransitionStatesAndProbs(state, action)
            mdp.getReward(state, action, nextState)
            mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        iteration = 0
        while iteration < self.iterations:
            states = self.mdp.getStates()
            citeration = util.Counter()
            for state in states:
                actions = self.mdp.getPossibleActions(state)
                q = util.Counter()
                if not self.mdp.isTerminal(state):
                    for action in actions:
                        q[action] = self.computeQValueFromValues(state, action)
                    citeration[state] = max(q.values())
            self.values = citeration
            iteration = iteration + 1

    def getValue(self, state):
        """
        Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        possible_transitions = self.mdp.getTransitionStatesAndProbs(state, action)
        q = 0
        for x in possible_transitions:
            q += x[1] * (
                self.mdp.getReward(state, action, x[0])
                + self.discount * self.values[x[0]]
            )
        return q
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        allActions = self.mdp.getPossibleActions(state)
        if self.mdp.isTerminal(state) or len(allActions) == 0:
            return None
        q = util.Counter()
        for action in allActions:
            q[action] = self.computeQValueFromValues(state, action)
        return q.argMax()
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
    * Please read learningAgents.py before reading this.*

    An AsynchronousValueIterationAgent takes a Markov decision process
    (see mdp.py) on initialization and runs cyclic value iteration
    for a given number of iterations using the supplied
    discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=1000):
        """
        Your cyclic value iteration agent should take an mdp on
        construction, run the indicated number of iterations,
        and then act according to the resulting policy. Each iteration
        updates the value of only one state, which cycles through
        the states list. If the chosen state is terminal, nothing
        happens in that iteration.

        Some useful mdp methods you will use:
            mdp.getStates()
            mdp.getPossibleActions(state)
            mdp.getTransitionStatesAndProbs(state, action)
            mdp.getReward(state)
            mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        iterCounter = 0
        while iterCounter < self.iterations:
            for state in self.mdp.getStates():
                q = util.Counter()
                for action in self.mdp.getPossibleActions(state):
                    q[action] = self.computeQValueFromValues(state, action)
                self.values[state] = q[q.argMax()]
                iterCounter += 1
                if iterCounter >= self.iterations:
                    return
        "*** YOUR CODE HERE ***"


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
    * Please read learningAgents.py before reading this.*

    A PrioritizedSweepingValueIterationAgent takes a Markov decision process
    (see mdp.py) on initialization and runs prioritized sweeping value iteration
    for a given number of iterations using the supplied parameters.
    """

    def __init__(self, mdp, discount=0.9, iterations=100, theta=1e-5):
        """
        Your prioritized sweeping value iteration agent should take an mdp on
        construction, run the indicated number of iterations,
        and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):

        mdp = self.mdp

        predecessors = {}
        priorityQueue = util.PriorityQueue()
        for state in mdp.getStates():
            qvalue = util.Counter()

            for action in self.mdp.getPossibleActions(state):
                T = self.mdp.getTransitionStatesAndProbs(state, action)
                for (nextState, prob) in T:
                    if prob != 0:
                        if nextState in predecessors:
                            predecessors[nextState].add(state)
                        else:
                            predecessors[nextState] = set()
                            predecessors[nextState].add(state)

                qvalue[action] = self.computeQValueFromValues(state, action)

            if not self.mdp.isTerminal(state):
                maxqvalue = qvalue[qvalue.argMax()]
                diff = abs(self.values[state] - maxqvalue)
                priorityQueue.update(state, -diff)

        for i in range(self.iterations):
            if priorityQueue.isEmpty():
                return

            state = priorityQueue.pop()

            if not self.mdp.isTerminal(state):
                qvalue = util.Counter()
                for action in self.mdp.getPossibleActions(state):
                    qvalue[action] = self.computeQValueFromValues(state, action)

                self.values[state] = qvalue[qvalue.argMax()]

            for p in predecessors[state]:
                qvaluep = util.Counter()
                for action in self.mdp.getPossibleActions(p):
                    qvaluep[action] = self.computeQValueFromValues(p, action)
                maxqvalue = qvaluep[qvaluep.argMax()]
                diff = abs(self.values[p] - maxqvalue)

                if diff > self.theta:
                    priorityQueue.update(p, -diff)

        "*** YOUR CODE HERE ***"
