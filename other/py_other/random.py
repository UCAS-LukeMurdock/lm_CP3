# Luke Murdock, Random Tests


import random as r
end = False
winU = False
winC = False
tie = False
shownBoard = ""

board = [
    [1, 2 ,3],
    [4, 5 ,6],
    [7, 8 ,9],
    ]

def check():
    global end
    global winU
    global winC
    global tie
    columnCheck = [0, 1, 2]
    columnX = 0

    # Ties
    tie = True
    end = True
    for row in board:
        for space in row:
            if space != "X" or space != "O":
                tie = False
                end = False

    # X Rows
    for row in board:
        if row == ["X", "X", "X"]:
            end = True
            winU = True
    # X Columns
    for columnNum in columnCheck:
        columnX = False
        for row in board:
            if row[columnNum] == "X":
                columnX += 1
            if columnX == 3:
                end = True
                winU = True
    # X Diagonal
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        end = True
        winU = True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        end = True
        winU = True

    # O Rows
    for row in board:
        if row == ["O", "O", "O"]:
            end = True
            winC = True
    # O Columns
    for columnNum in columnCheck:
        for row in board:
            columnX = False
            if row[columnNum] == "O":
                columnX += 1
            if columnX == 3:
                end = True
                winC = True
    # O Diagonal
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        end = True
        winC = True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        end = True
        winC = True


print("Welcome to Tic-Tac-Toe! In this game you will play against a computer by deciding which space(number) to place your X's.")
while True:
    correctSpot = False

    for row in board:
        print(row)
    check()
    if end == True:
        break

    choiceU = input("Where do you want to place X?\n")
    for rowIndex, row in enumerate(board):
        for spaceIndex, space in enumerate(row):
            if str(space) == choiceU:
                board[rowIndex][spaceIndex] = "X"
    for row in board:
        print(row)
    check()
    if end == True:
        break

    while correctSpot == False:
        choiceC = r.randrange(1, 10)
        for rowIndex, row in enumerate(board):
            for spaceIndex, space in enumerate(row):
                if str(space) == str(choiceC):
                    board[rowIndex][spaceIndex] = "O"
                    correctSpot = True

    print("")

if winU == True:
    print("You Won!")
elif winC == True:
    print("You Lost!")
elif tie == True:
    print("Draw!")