import sys
size = 8
board = []

def createBoard(board):
    for i in range(size):
        board.append(['.'] * 8)
    return board

def resetBoard(board):
    for i in range(size):
        for j in range(size):
            board[i][j] = '.'
    half = size // 2
    board[half-1][half-1] = 'W'
    board[half][half] = 'W'
    board[half-1][half] = 'B'
    board[half][half-1] = 'B'

def displayBoard(board):
    print("  a  b  c  d  e  f  g  h")
    for i in range(size):
        print(i + 1, end = " ")
        for j in range(size):
            print(board[i][j], end = '  ')
        print('\n')
def isOnBoard(x, y):
    return x >= 0 and y >= 0 and x < size and y <size


def isValidMove(board, tile, xStart, yStart):
    if board[xStart][yStart] != "." or not isOnBoard(xStart, yStart):
        return False
    board[xStart][yStart] = tile
    if tile == 'B':
        otherTile = 'W'
    else:
        otherTile = 'B'
    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1],[-1, -1], [-1, 0], [-1, 1]]:
        x, y = xStart, yStart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xStart and y == yStart:
                            break
                        tilesToFlip.append([x, y])
    board[xStart][yStart] = '.'
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip
def getValidMoves(board, tile):
    validMoves = []
    for i in range(size):
        for j in range(size):
            if isValidMove(board, tile, i, j) != False:
                validMoves.append([j, i])
    return validMoves

def Move(board, tile, xStart, yStart):
    tilesToFlip = isValidMove(board, tile, xStart, yStart)
    if tilesToFlip == False:
        return False
    board[xStart][yStart] = tile
    for i, j in tilesToFlip:
        board[i][j] = tile
    return True

def getMove(board, playerTile):
    #Valid choices
    c = '1 2 3 4 5 6 7 8'.split()
    s = 'a b c d e f g h'.split()
    while 1:
        x = 0
        y = 0
        mv = input().lower()
        if mv == "q":
            return 'q'
        if len(mv) < 2:
            print('Player ' + playerTile + ": ",end = '')
            continue
        move = []
        if mv == '':
            continue
        move.append(mv[0])
        move.append(mv[1])
        for i in range(len(s)):
            if move[0] == s[i]:
                move[0] = str(i + 1)
                break
        if len(move) == 2 and move[0] in c and move[1] in c:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, y, x) != False:
                break
            else:
                print('Player ' + playerTile + ": ",end = '')
                continue
        else:
            print("\nPlayer " + playerTile + ": ",end = '')
    return [y, x]
def toadochu(toadoso): #[x,y]
    s = 'a b c d e f g h'.split()
    for i in range(len(s)):
        if i == toadoso[0]:
            a = ''
            a = str(s[i]) + str(toadoso[1] + 1)
            return a


while True:
    # Reset the board and game.
    board = createBoard(board)
    resetBoard(board)
    # displayBoard(board)
    player1 = "B"
    player2 = "W"
    turn = "B"


    while 1:
        if turn == "B":
            displayBoard(board)
            print('Valid choices: ',end = '')
            validMoves = getValidMoves(board, player1)
            a = []
            for i in range(len(validMoves)):
                a.append(toadochu(validMoves[i]))
            for i in range(len(a)):
                print(a[i],end = '')
                if i < len(a) - 1:
                    print(end = ' ')


            print("\nPlayer " + turn + ": ",end = '')
            move = getMove(board, player1)
            if move == "q":
                sys.exit()
            else:
                Move(board, player1, move[0], move[1])
            if validMoves == []:
                print('Player B cannot play.')
                break
            else:
                turn = "W"
        else:
            displayBoard(board)
            print('Valid choices: ',end = '')
            validMoves = getValidMoves(board, player2)
            a = []
            for i in range(len(validMoves)):
                a.append(toadochu(validMoves[i]))
            for i in range(len(a)):
                print(a[i],end = '')
                if i < len(a) - 1:
                    print(end = ' ')

            print("\nPlayer " + turn + ": ",end = '')
            move = getMove(board, player2)
            if move == "q":
                sys.exit()
            else:
                Move(board, player2, move[0], move[1])
            if validMoves == []:
                print('Player W cannot play.')
                break
            else:
                turn = "B"
BScore = 0
WScore = 0
for x in range(size):
    for y in range(size):
        if board[x][y] == 'B':
            BScore += 1
        if board[x][y] == 'W':
            WScore += 1
print("End of the game. W: " + WScore + ", B: " + BScore )
if BScore > WScore:
    print('B wins.')
else:
    print('W wins.')
