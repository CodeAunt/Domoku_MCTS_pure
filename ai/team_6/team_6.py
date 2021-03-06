##
# team_6
# For Midterm Project
#

import numpy as np
from goboard import Player, BoardInfo, GuiManager
from math import *
import random
import copy
from operator import itemgetter


def rollout_policy_fn(board):
    """a coarse, fast version of policy_fn used in the rollout phase."""
    # rollout randomly
    # action_probs = np.random.rand(len(board.availables))
    action_probs = np.random.rand(len(board.availables))
    return zip(board.availables, action_probs)

<<<<<<< HEAD

=======
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
def policy_value_fn(board):
    """a function that takes in a state and outputs a list of (action, probability)
    tuples and a score for the state"""
    # return uniform probabilities and 0 score for pure MCTS
<<<<<<< HEAD
    action_probs = np.ones(len(board.availables)) / len(board.availables)
    return zip(board.availables, action_probs), 0


=======
    action_probs = np.ones(len(board.availables))/len(board.availables)
    return zip(board.availables, action_probs), 0

>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
class plate(object):
    def __init__(self, **kwargs):
        self.width = int(kwargs.get('width', 13))
        self.height = int(kwargs.get('height', 13))
        # board states stored as a dict,
        # key: move as location on the board,
        # value: player as pieces type
        self.states = {}
        # need how many pieces in a row to win
<<<<<<< HEAD
        self.availables = list(range(self.width * self.height))
=======
        self.availables = []
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
        self.n_in_row = int(kwargs.get('n_in_row', 5))
        self.players = [1, 2]  # player1 and player2
        self.current_player = 2

<<<<<<< HEAD
=======

>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
    def init_board(self, start_player=0):
        if self.width < self.n_in_row or self.height < self.n_in_row:
            raise Exception('board width and height can not be '
                            'less than {}'.format(self.n_in_row))
        self.current_player = self.players[start_player]  # start player
        # keep available moves in a list
        self.availables = list(range(self.width * self.height))
        self.states = {}
        self.last_move = -1

    def move_to_location(self, move):
        """
        3*3 board's moves like:
        6 7 8
        3 4 5
        0 1 2
        and move 5's location is (1,2)
        """
        h = move // self.width
        w = move % self.width
        return [h, w]

    def location_to_move(self, location):
        if len(location) != 2:
            return -1
        h = location[0]
        w = location[1]
        move = h * self.width + w
        if move not in range(self.width * self.height):
            return -1
        return move

    def current_state(self):
        """return the board state from the perspective of the current player.
        state shape: 4*width*height
        """

        square_state = np.zeros((4, self.width, self.height))
        if self.states:
            moves, players = np.array(list(zip(*self.states.items())))
            move_curr = moves[players == self.current_player]
            move_oppo = moves[players != self.current_player]
            square_state[0][move_curr // self.width,
                            move_curr % self.height] = 1.0
            square_state[1][move_oppo // self.width,
                            move_oppo % self.height] = 1.0
            # indicate the last move location
            square_state[2][self.last_move // self.width,
                            self.last_move % self.height] = 1.0
        if len(self.states) % 2 == 0:
            square_state[3][:, :] = 1.0  # indicate the colour to play
        return square_state[:, ::-1, :]

    def do_move(self, move):
        self.states[move] = self.current_player
        self.availables.remove(move)
        self.current_player = (
            self.players[0] if self.current_player == self.players[1]
            else self.players[1]
        )
        self.last_move = move

    def has_a_winner(self):
        width = self.width
        height = self.height
        states = self.states
        n = self.n_in_row

<<<<<<< HEAD
        # moved = list(set(range(width * height)) - set(self.availables))
        moved = states.keys()
=======
        moved = list(set(range(width * height)) - set(self.availables))
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
        if len(moved) < self.n_in_row + 2:
            return False, -1

        for m in moved:
            h = m // width
            w = m % width
            player = states[m]

            if (w in range(width - n + 1) and
<<<<<<< HEAD
                        len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
                return True, player

            if (h in range(height - n + 1) and
                        len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
                return True, player

            if (w in range(width - n + 1) and h in range(height - n + 1) and
                        len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
                return True, player

            if (w in range(n - 1, width) and h in range(height - n + 1) and
                        len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
=======
                    len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
                return True, player

            if (h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
                return True, player

            if (w in range(width - n + 1) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
                return True, player

            if (w in range(n - 1, width) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
                return True, player

        return False, -1

    def game_end(self):
        """Check whether the game is ended or not"""
        win, winner = self.has_a_winner()
        if win:
            return True, winner
        elif not len(self.availables):
            return True, -1
        return False, -1

    def get_current_player(self):
        return self.current_player

<<<<<<< HEAD

=======
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
# board dense 0 1
# board steps (x, y) k/w

# board avaliable index
# board index and player
def transform(board):
    states = {}
<<<<<<< HEAD
    #availables = list(range(board.size_x * board.size_y))
=======
    availables = list(range(board.size_x * board.size_y))
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
    x = 0
    y = 0
    c = 'k'
    for step in board.steps:
        ((x, y), c) = step
<<<<<<< HEAD
        states.update({(x * 13 + y): (2 if c == 'k' else 1)})
        #availables.remove(x * 13 + y)
    return states, x * 13 + y, (2 if c == 'k' else 1)
=======
        states.update({(x * 13 + y): (2 if c =='k' else 1 )})
        availables.remove(x * 13 + y)
    return states, availables, x * 13 + y, (2 if c =='k' else 1)
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1

    # availables = board.steps[]
    # board.dense
    # return

<<<<<<< HEAD

=======
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
# def judge(board):
#     width = board.width
#     height = board.height
#     states = board.states
#     n = 5 #self.n_in_row
#
#     moved = list(set(range(width * height)) - set(self.availables))
#     if len(moved) < 5 + 2:
#         return False, -1
#
#     for m in moved:
#         h = m // width
#         w = m % width
#         player = states[m]
#
#         if (w in range(width - n + 1) and
#                     len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
#             return True, player
#
#         if (h in range(height - n + 1) and
#                     len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
#             return True, player
#
#         if (w in range(width - n + 1) and h in range(height - n + 1) and
#                     len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
#             return True, player
#
#         if (w in range(n - 1, width) and h in range(height - n + 1) and
#                     len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
#             return True, player
#
#     return False, -1
#
#     return


class TreeNode(object):
    """A node in the MCTS tree. Each node keeps track of its own value Q,
    prior probability P, and its visit-count-adjusted prior score u.
    """

    def __init__(self, parent, prior_p):
        self._parent = parent
        self._children = {}  # a map from action to TreeNode
        self._n_visits = 0
        self._Q = 0
        self._u = 0
        self._P = prior_p

    def expand(self, action_priors):
        """Expand tree by creating new children.
        action_priors: a list of tuples of actions and their prior probability
            according to the policy function.
        """
        for action, prob in action_priors:
            if action not in self._children:
                self._children[action] = TreeNode(self, prob)

<<<<<<< HEAD
=======

>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
    def select(self, c_puct):
        """Select action among children that gives maximum action value Q
        plus bonus u(P).
        Return: A tuple of (action, next_node)
        """
        return max(self._children.items(),
                   key=lambda act_node: act_node[1].get_value(c_puct))

    def update(self, leaf_value):
        """Update node values from leaf evaluation.
        leaf_value: the value of subtree evaluation from the current player's
            perspective.
        """
        # Count visit.
        self._n_visits += 1
        # Update Q, a running average of values for all visits.
<<<<<<< HEAD
        self._Q += 1.0 * (leaf_value - self._Q) / self._n_visits
=======
        self._Q += 1.0*(leaf_value - self._Q) / self._n_visits
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1

    def update_recursive(self, leaf_value):
        """Like a call to update(), but applied recursively for all ancestors.
        """
        # If it is not root, this node's parent should be updated first.
        if self._parent:
            self._parent.update_recursive(-leaf_value)
        self.update(leaf_value)

    def get_value(self, c_puct):
        """Calculate and return the value for this node.
        It is a combination of leaf evaluations Q, and this node's prior
        adjusted for its visit count, u.
        c_puct: a number in (0, inf) controlling the relative impact of
            value Q, and prior probability P, on this node's score.
        """
        self._u = (c_puct * self._P *
                   np.sqrt(self._parent._n_visits) / (1 + self._n_visits))
        return self._Q + self._u

    def is_leaf(self):
        """Check if leaf node (i.e. no nodes below this have been expanded).
        """
        return self._children == {}

    def is_root(self):
        return self._parent is None


class MCTS(object):
    """A simple implementation of Monte Carlo Tree Search."""

    def __init__(self, policy_value_fn, c_puct=2, n_playout=5):
        """
        policy_value_fn: a function that takes in a board state and outputs
            a list of (action, probability) tuples and also a score in [-1, 1]
            (i.e. the expected value of the end game score from the current
            player's perspective) for the current player.
        c_puct: a number in (0, inf) that controls how quickly exploration
            converges to the maximum-value policy. A higher value means
            relying on the prior more.
        """
        self._root = TreeNode(None, 1.0)
        self._policy = policy_value_fn
        self._c_puct = c_puct
        self._n_playout = n_playout

    def _playout(self, state):
        """Run a single playout from the root to the leaf, getting a value at
        the leaf and propagating it back through its parents.
        State is modified in-place, so a copy must be provided.
        """
        node = self._root
<<<<<<< HEAD
        while (1):
            if node.is_leaf():
=======
        while(1):
            if node.is_leaf():

>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
                break
            # Greedily select next move.
            action, node = node.select(self._c_puct)
            state.do_move(action)

        action_probs, _ = self._policy(state)
        # Check for end of game
        end, winner = state.game_end()
        if not end:
            node.expand(action_probs)
        # Evaluate the leaf node by random rollout
        leaf_value = self._evaluate_rollout(state)
        # Update value and visit count of nodes in this traversal.
        node.update_recursive(-leaf_value)

<<<<<<< HEAD
=======

>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
    def _evaluate_rollout(self, state, limit=1000):
        """Use the rollout policy to play until the end of the game,
        returning +1 if the current player wins, -1 if the opponent wins,
        and 0 if it is a tie.
        """
        player = state.get_current_player()
        for i in range(limit):
            end, winner = state.game_end()
            if end:
                break
            action_probs = rollout_policy_fn(state)
            max_action = max(action_probs, key=itemgetter(1))[0]
            state.do_move(max_action)
        else:
            # If no break from the loop, issue a warning.
            print("WARNING: rollout reached move limit")
        if winner == -1:  # tie
            return 0
        else:
            return 1 if winner == player else -1

    def get_move(self, state):
        """Runs all playouts sequentially and returns the most visited action.
        state: the current game state

        Return: the selected action
        """
        for n in range(self._n_playout):
            state_copy = copy.deepcopy(state)
            self._playout(state_copy)
            print(n)
        print("Judge done")
        return max(self._root._children.items(),
                   key=lambda act_node: act_node[1]._n_visits)[0]

    def update_with_move(self, last_move):
        """Step forward in the tree, keeping everything we already know
        about the subtree.
        """
        if last_move in self._root._children:
            self._root = self._root._children[last_move]
            self._root._parent = None
        else:
            self._root = TreeNode(None, 1.0)

    def __str__(self):
        return "MCTS"

<<<<<<< HEAD

##########################################################################

# def UCTPlayGame():
class Ai(Player):
    def __init__(self, color, **kwargs):
        super(Ai, self).__init__(color)
        # self.mcts = MCTS(policy_value_fn, c_puct, n_playout)
        self.mcts = MCTS(policy_value_fn, c_puct=5, n_playout=600)
=======
##########################################################################

#def UCTPlayGame():
class Ai(Player):
    def __init__(self, color, **kwargs):
        super(Ai, self).__init__(color)
        #self.mcts = MCTS(policy_value_fn, c_puct, n_playout)
        self.mcts = MCTS(policy_value_fn, c_puct=5, n_playout=1000)
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
        self.player = 2
        try:
            size_x, size_y = kwargs['board_size']
            self.value = np.zeros((size_x, size_y))
        except IndexError:
            self.value = np.zeros((13, 13))

    def set_player_ind(self, p):
        self.player = p

    def reset_player(self):
        self.mcts.update_with_move(-1)

    def get_action(self, board: BoardInfo, timeout) -> (int, int):
        platex = plate(width=13, height=13, n_in_row=5)
<<<<<<< HEAD
        platex.states, platex.last_move, platex.current_player = transform(board)
        steps = platex.states.keys()
        avastored = []
        for step in steps:
            for i in [step - 14, step - 13, step - 12, step - 1, step + 1, step + 12, step + 13, step + 14]:
                if i not in avastored and i not in steps and i >= 0 and i < 169:
                    avastored.append(i)
        platex.availables = avastored
        platex.current_player = 3 - platex.current_player
        # sensiblves = plae_motex.availables
=======
        platex.states, platex.availables, platex.last_move, platex.current_player = transform(board)
        platex.current_player = 3 - platex.current_player
        sensible_moves = platex.availables

>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
        if len(board.steps) == 0:
            return 6, 7
        if len(board.steps) < 169:
            move = self.mcts.get_move(platex)
<<<<<<< HEAD
            print(int(move / 13), move % 13)
            self.mcts.update_with_move(-1)
            if board.is_legal_action(int(move / 13), move % 13):
                print("legal")
                return int(move / 13), move % 13
=======
            print(int(move/13), move%13)
            self.mcts.update_with_move(-1)
            if board.is_legal_action(int(move/13), move%13):
                print("legal")
                return int(move/13), move%13
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
            else:
                print("Fuck piece")
        else:
            print("WARNING: the board is full")

    def __str__(self):
        return "MCTS {}".format(self.player)

<<<<<<< HEAD
        # def get_action(self, board: BoardInfo, timeout) -> (int, int):
=======
    #def get_action(self, board: BoardInfo, timeout) -> (int, int):
>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1

        """
            Implement your algorithm here.

            **Important**
            1. You must return (x, y)
            2. If any exception is raised, you will lose the game directly. Use try-except to handle error/exception.
            3. To get current state of the game, you could call board.dense or board.steps to get data.
            # dense store where have be occupied (placement), to detect collisions
            # steps store each steps in a game

            :return: int x, int y
            """

# for x in range(0, board.size_x):
#     for y in range(0, board.size_y):
#         if board.is_legal_action(x, y):
#             return x, y
#         else:
#             continue
<<<<<<< HEAD
=======








>>>>>>> 6aeca25084a81bb0cbe3b878b7240f6e0de7d1a1
