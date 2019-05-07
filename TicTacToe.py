import random

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter =='X' or letter =='O'):
        print('Pick X or O.')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
def playAgain():
    print('Play Again? (y/n)')
    return input().lower()

def makeMove(board, letter, move):
    board[move] = letter

def winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

def copyBoard(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def freeSpace(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
        print('next move? (1-9)')
        move = input()
    return int(move)

def makeRandomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if freeSpace(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        copy = copyBoard(board)
        if freeSpace(copy, i):
            makeMove(copy, computerLetter, i)
            if winner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = copyBoard(board)
        if freeSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if winner(copy, playerLetter):
                print(i)
    move = makeRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move
    if freeSpace(board, 5):
        return 5
    return makeRandomMove(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if freeSpace(board, i):
            return False
    return True


while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('the ' + turn + ' will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("You Win!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Tie Game")
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if winner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("You Lose!")
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Tie Game")
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
