moves = 0
players = ["X",  "O"]
winner = None
currentPlayer = players[0]
board = [
    '', '', '',
    '', '', '',
    '', '', ''
]


def printBoard(board):
    print(board[0], ' | ', board[1], ' | ', board[2])
    print('---------')
    print(board[3], ' | ', board[4], ' | ', board[5])
    print('---------')
    print(board[6], ' | ', board[7], ' | ', board[8])


def switchPlayer():
    global currentPlayer
    currentPlayer = players[1] if currentPlayer == players[0] else players[0]


def playerInput(board):
    inp = int(input('enter a position number 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '':
        board[inp-1] = currentPlayer
        return True
    else:
        print('invalid position')
        return False


def checkHorizontale(board):
    global winner
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != '':
            winner = board[i]
            return True
    return False


def checkVertical(board):
    global winner
    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] and board[i] != '':
            winner = board[i]
            return True
    return False


def checkDiagonal(board):
    global winner
    diags = {0: [0, 4, 8], 2: [2, 4, 6]}
    for i in diags:
        if board[diags[i][0]] == board[diags[i][1]] == board[diags[i][2]] and board[i] != '':
            winner = board[diags[i][0]]
            return True
    return False


def checkWinner(board):
    if checkHorizontale(board) or checkVertical(board) or checkDiagonal(board):
        print('Winner is ' + winner)


def checkTie(board):
    global winner
    global moves

    if (moves >= 6 and winner is None) or ('' not in board):
        winner = 'tie'
        print('It\'s a tie!')
        return True
    return False


def checkGame(board):
    global moves
    moves += 1
    if checkWinner(board) or checkTie(board):
        printBoard(board)


while winner == None:
    printBoard(board)
    while playerInput(board) == False:
        printBoard(board)
    switchPlayer()
    checkGame(board)
