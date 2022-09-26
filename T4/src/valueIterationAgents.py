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
from copy import deepcopy


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

        # Write value iteration code here
        for i in range(self.iterations):
            new_values = deepcopy(self.values)
            for s in self.mdp.getStates():
                action_values = util.Counter()
                possible_actions = self.mdp.getPossibleActions(s)
                if possible_actions:
                    for a in self.mdp.getPossibleActions(s):
                        for p in self.mdp.getTransitionStatesAndProbs(s, a):
                            action_values[a] = action_values[a] + p[1]*self.getValue(p[0])
                    # Vk+1(s) = R(s) + Y*max(sum(P(s'|s,a)*Vk(s')))
                    new_values[s] = self.mdp.getReward(s, None, None) + self.discount * action_values[action_values.argMax()]
            self.values = new_values

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        # If action is exit, Q-value == Reward
        if action == "exit":
            return self.mdp.getReward(state, None, None)

        q_value = 0
        for p in self.mdp.getTransitionStatesAndProbs(state, action):
            # Q(s,a) = sum(P(s'|s,a) * Y * V(s'))
            q_value = q_value + p[1]*self.discount*self.getValue(p[0])
        return q_value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        possible_actions = self.mdp.getPossibleActions(state)
        if not possible_actions:
            return None
        action_values = util.Counter()
        for a in possible_actions:
            for p in self.mdp.getTransitionStatesAndProbs(state, a):
                # Best action is the one that will lead to a state with max reward
                # value of the action = sum(P(s'|s,a)*V(s'))
                action_values[a] = action_values[a] + p[1]*self.getValue(p[0])
        return action_values.argMax()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
