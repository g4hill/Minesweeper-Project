#this function sets up the gameboard for the losing condition
def setUpLoss(topBoard, bottomBoard, bWidth, bHeight):
    checkY = 0

    while checkY < bHeight:
        checkX = 0
        while checkX < bWidth:
            #if there is a mine at this current position, set this position at topBoard to 'o' (so that topBoard gets ignored when drawing the gameboard)
            if bottomBoard[checkY][checkX] == '*':
                topBoard[checkY][checkX] = 'o'
            #if we've flagged a position that isn't a mine, then display the false-flagged icon on bottomBoard (and ignore topBoard, of course) 
            elif topBoard[checkY][checkX] == 'F' and bottomBoard[checkY][checkX] != '*':
                topBoard[checkY][checkX] = 'o'
                bottomBoard[checkY][checkX] = 'r'
            checkX += 1
        checkY += 1