#this file is meant for code related to gameboard creation

#imports
import random
import countAdj

#the main function for this file - places the mines and numbers in bottomBoard
def setup(bottomBoard, bWidth, bHeight, numMines, startX, startY):
    #sets every square in the starting area to be "S", so that no mines get placed there
    createStartSquare(bottomBoard, startX, startY, bWidth, bHeight, "S")
    
    for i in range(numMines):
        #gets a random x and y position, and reassigns them if they're in the starting area or on another mine
        randX = random.randrange(0, bWidth)
        randY = random.randrange(0, bHeight)
        while bottomBoard[randY][randX] == '*' or bottomBoard[randY][randX] == 'S':
            randX = random.randrange(0, bWidth)
            randY = random.randrange(0, bHeight)
        
        #puts down a new mine
        bottomBoard[randY][randX] = '*'
    
    #sets every square in the starting area back to normal
    createStartSquare(bottomBoard, startX, startY, bWidth, bHeight, '-')

    #for every square in the board...
    countY = 0
    while countY < bHeight:
        countX = 0
        while countX < bWidth:
            #if the square is not a mine...
            if bottomBoard[countY][countX] != '*':
                #find out how many mines are adjacent to it, and set the squares value to the number of adjacent mines if the number is nonzero
                count = countAdj.countAdj(bottomBoard, countX, countY, bWidth, bHeight)
                if count != 0:
                    bottomBoard[countY][countX] = count
            countX += 1
        countY += 1

#sets every possible adjacent value (depending on the inputs) to be char
def createStartSquare(bottomBoard, posX, posY, bWidth, bHeight, char):
    #if we're looking at a space on the top row of the board
    if posY == 0:
        #if we're looking at a space on the lefmost column of the board
        if posX == 0:
            #set all possible adjacent tiles to char
            bottomBoard[posY][posX] = char
            bottomBoard[posY][posX + 1] = char
            bottomBoard[posY + 1][posX] = char
            bottomBoard[posY + 1][posX + 1] = char
        
        #if we're looking at a space on the rightmost column of the board
        elif posX == bWidth - 1:
            #set all possible adjacent tiles to char
            bottomBoard[posY][posX] = char
            bottomBoard[posY][posX - 1] = char
            bottomBoard[posY + 1][posX] = char
            bottomBoard[posY + 1][posX - 1] = char

        #if we're looking at a space in a middle column (i.e. not the rightmost or leftmost column) of the board
        else:
            #set all possible adjacent tiles to char
            bottomBoard[posY][posX - 1] = char
            bottomBoard[posY][posX] = char
            bottomBoard[posY][posX + 1] = char
            bottomBoard[posY + 1][posX - 1] = char
            bottomBoard[posY + 1][posX] = char
            bottomBoard[posY + 1][posX + 1] = char

    #if we're looking at a space on the bottom 
    elif posY == bHeight - 1:
        #if we're looking at a space on the leftmost column of the board
        if posX == 0:
            #set all possible adjacent tiles to char
            bottomBoard[posY][posX] = char
            bottomBoard[posY][posX + 1] = char
            bottomBoard[posY - 1][posX] = char
            bottomBoard[posY - 1][posX + 1] = char
        
        #if we're looking at a space on the rightmost column of the board
        elif posX == bWidth - 1:
            #set all possible adjacent tiles to char
            bottomBoard[posY][posX] = char
            bottomBoard[posY][posX - 1] = char
            bottomBoard[posY - 1][posX] = char
            bottomBoard[posY - 1][posX - 1] = char

        #if we're looking at a space in a middle column
        else:
            #set all possible adjacent tiles to char
            bottomBoard[posY][posX - 1] = char
            bottomBoard[posY][posX] = char
            bottomBoard[posY][posX + 1] = char
            bottomBoard[posY - 1][posX - 1] = char
            bottomBoard[posY - 1][posX] = char
            bottomBoard[posY - 1][posX + 1] = char
    
    #if we're looking at a space in a middle row, (i.e. not on the top or bottom of the board) and in the leftmost column
    elif posX == 0:
        #set all possible adjacent tiles to char
        bottomBoard[posY - 1][posX] = char
        bottomBoard[posY - 1][posX + 1] = char
        bottomBoard[posY][posX] = char
        bottomBoard[posY][posX + 1] = char
        bottomBoard[posY + 1][posX] = char
        bottomBoard[posY + 1][posX + 1] = char

    #if we're looking at a space in a middle row, and in the rightmost column
    elif posX == bWidth - 1:
        #set all possible adjacent tiles to char
        bottomBoard[posY - 1][posX] = char
        bottomBoard[posY - 1][posX - 1] = char
        bottomBoard[posY][posX] = char
        bottomBoard[posY][posX - 1] = char
        bottomBoard[posY + 1][posX] = char
        bottomBoard[posY + 1][posX - 1] = char

    #if we're looking at a space in a middle row and in a middle column
    else:
        #set all possible adjacent tiles to char
        bottomBoard[posY - 1][posX - 1] = char
        bottomBoard[posY - 1][posX] = char
        bottomBoard[posY - 1][posX + 1] = char
        bottomBoard[posY][posX - 1] = char
        bottomBoard[posY][posX] = char
        bottomBoard[posY][posX + 1] = char
        bottomBoard[posY + 1][posX - 1] = char
        bottomBoard[posY + 1][posX] = char
        bottomBoard[posY + 1][posX + 1] = char