from tictactoe import initial_state, player, actions, result, winner, terminal, minimax
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

board = initial_state()

turn = player(board)


res = result(board, (1,1))


l = [[X, X, O],
     [O, O, X],
     [X, O, X]]
minimax(board)
