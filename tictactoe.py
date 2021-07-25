"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    # return [[O, EMPTY, X],
    #         [X, X, O],
    #         [EMPTY, O, EMPTY]]

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    
    if x_count > o_count:
        return O
    # elif o_count > x_count:
    #     return X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []

    for i,row in enumerate(board):
        for j,col in enumerate(row):
            if not board[i][j]:
                action.append((i,j))

    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = []
    x,y = action
    turn = player(board)

    for i,row in enumerate(board):
        tmp = []
        for j,col in enumerate(row):
            if x == i and y == j:
                tmp.append(turn)
            else:
                tmp.append(col)
        
        new_board.append(tmp)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    inverted_board = []

    for i,row in enumerate(board):
        tmp = []
        for j,col in enumerate(row):
            tmp.append(board[j][i])
        
        inverted_board.append(tmp)

    for row in board:
        if row.count("X") == 3:
            return X
        elif row.count("O") == 3:
            return O
    
    for row in inverted_board:
        if row.count("X") == 3:
            return X
        elif row.count("O") == 3:
            return O

    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for row in board:
        for col in row:
            if not col:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)

    if won == X:
        return 1
    elif won == O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    turn = player(board)

    if turn == X:
        moves =  max_value(board)

        print(moves, 1)
        # moves.sort(key=lambda a : a[1], reverse=True)
        return moves[0 ]

    else:
        moves = min_value(board)
        print(moves, 2)
        # moves.sort(key=lambda a : a[1])
        return moves[0]

def max_value(board):
    max_results = []

    if terminal(board):
        return (1,utility(board))

    for action in actions(board):
        value = min_value(result(board,action))
        max_results.append((action, value[1]))

    max_results.sort(key=lambda a:a[1], reverse=True)    
    return max_results[0]


def min_value(board):
    min_results = []
    
    if terminal(board):
        return (1,utility(board))

    for action in actions(board):
        value = max_value(result(board,action))
        min_results.append((action,value[1]))
        
    min_results.sort(key=lambda a:a[1])
    return min_results[0]
