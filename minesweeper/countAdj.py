#this function counts the number of adjacent mines for a given space
def countAdj(gameBoard, x, y, boardWidth, boardHeight):
    counter = 0

    #represents the board position of the left and right spaces of the space we are looking at
    fC = x - 1
    tC = x + 1
    
    #represents the board position of the above and below spaces of the space we are looking at
    tR = y - 1
    bR = y + 1

    #if there are spaces above the space we are looking at
    if(tR >= 0):
        #if there are spaces to the left of the space we are looking at
        if(fC >= 0):
            #if the top left adjacent space to the space we are looking at contains a mine, increase the counter by 1 
            if(gameBoard[tR][fC] == '*'):
                counter += 1
        
        #if the space directly above the space we are looking at contains a mine, increase the counter by 1
        if(gameBoard[tR][x] == '*'):
            counter += 1

        #if there are spaces to the right of the space we are looking at
        if(tC < boardWidth):
            #if the top right adjacent space to the space we are looking at contains  mine, increase the counter by 1
            if(gameBoard[tR][tC] == '*'):
                counter += 1
    
    #if there are spaces to the left of the space we are looking at
    if(fC >= 0):
        #if the space to the left of the space we are looking at contains a mine, increase the counter by 1
        if(gameBoard[y][fC] == '*'):
            counter += 1
    
    #if there are spaces to the right of the space we are looking at
    if(tC < boardWidth):
        #if the space to the right of the space we are looking at contains a mine, increase the counter by 1
        if(gameBoard[y][tC] == '*'):
            counter += 1
    
    #if there are spaces below the space we are looking at
    if(bR < boardHeight):
        #if there are spaces to the left of the space we are looking at
        if(fC >= 0):
            #if the space to the bottom left of the space we are looking at contains a mine, increase the counter by 1
            if(gameBoard[bR][fC] == '*'):
                counter += 1
        #if the space directly below the space we are looking at contains a mine, increase the counter by 1
        if(gameBoard[bR][x] == '*'):
            counter += 1
        #if there are spaces to the right of the space we are looking at
        if(tC < boardWidth):
            #if the space to the bottom right of the space we are looking at cont
            if(gameBoard[bR][tC] == '*'):
                counter += 1

    return counter