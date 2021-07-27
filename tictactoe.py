"""
Tic Tac Toe Player
"""

import math
from random import randint

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
    x_count = 0
    o_count = 0

    #Count no of X and no of O in the board
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    
    #Find the turn
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action = []

    #Find empty cells in the board
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

    #Fill on certain cell and return the resulting board
    for i,row in enumerate(board):
        tmp = []
        for j,col in enumerate(row):
            if x == i and y == j:
                if col:
                    raise Exception("Invalid Move")

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

    #Invert the board
    for i,row in enumerate(board):
        tmp = []
        for j,col in enumerate(row):
            tmp.append(board[j][i])
        
        inverted_board.append(tmp)

    #Check if three rows are same or not
    for row in board:
        if row.count("X") == 3:
            return X
        elif row.count("O") == 3:
            return O
    
    #Agian for the inverted board
    for row in inverted_board:
        if row.count("X") == 3:
            return X
        elif row.count("O") == 3:
            return O

    #Check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    #No-winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    #Check if any cell is empty
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

    #1,0,-1
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

    #The first move
    elif board == initial_state():
        return [(0,0),(0,2),(1,1),(2,0),(2,2)][randint(0,4)]
    
    #Whose turn
    turn = player(board)

    #If AI is X
    if turn == X:
        moves =  max_value(board)
        return moves[0]

    #If AI is Y
    else:
        moves = min_value(board)
        return moves[0]


def max_value(board):
    """ 
        IF AI is X, find it's optimal move.
    """
    max_results = []

    #If game-over, return utility of the board
    if terminal(board):
        return (1,utility(board))

    #Find all possible moves(recursion)
    for action in actions(board):

        #Get the value of the previous state
        value = min_value(result(board,action))
        
        #Alpha-Beta Pruning
        if value == 1:
            return ((action), value)
        
        max_results.append((action, value[1]))

    #Return the best action
    max_results.sort(key=lambda a:a[1], reverse=True)    
    return max_results[0]


def min_value(board):
    """ 
        IF AI is Y, find it's optimal move.
    """
    min_results = []
    
    #If game-over, return utility of the board
    if terminal(board):
        return (1,utility(board))

    #Find all possible moves(recursion)
    for action in actions(board):

        #Get the value of the previous state
        value = max_value(result(board,action))
        
        #Alpha-Beta Pruning
        if value == -1:
            return ((action), value)

        min_results.append((action,value[1]))

    #Return the best action
    min_results.sort(key=lambda a:a[1])
    return min_results[0]
