"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nox = 0
    noo = 0

    for row in board:
        nox += row.count(X)
        noo += row.count(O)
    if nox == 0:
        return X
    elif nox > noo:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row in range(3):
        for cell in range(3):
            if board[row][cell] == EMPTY:
                actions.add((row,cell))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")


    nboard = deepcopy(board)
    play = player(board)

    nboard[action[0]][action[1]] = play

    return nboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for row in board:
        if row[0] == X and row[1] == X and row[2] == X:
            return X
        elif row[0] == O and row[1] == O and row[2] == O:
            return O

    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
        
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif len(actions(board)) == 0:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def MAXValue(board):
        if terminal(board):
            return utility(board)
        v = -math.inf

        for action in actions(board):
            v = max(v, MINValue(result(board,action)))
        return v



    def MINValue(board):
        if terminal(board):
            return utility(board)
        v = math.inf

        for action in actions(board):
            v = min(v, MAXValue(result(board,action)))
        return v



    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            l = MINValue(result(board,action))
            if l >= v:
                v = l
                optimal_action = action
        return optimal_action
    
    else:
        v = math.inf
        for action in actions(board):
            l = MAXValue(result(board,action))
            if l <= v:
                v = l
                optimal_action = action
        return optimal_action
        
