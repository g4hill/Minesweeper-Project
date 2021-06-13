#this file contains the functions that check the two ways that we can win

#this function checks to see if we've flagged every single mine
def checkWin(bottomBoard, topBoard, bWidth, bHeight):
    checkY = 0
    
    while checkY < bHeight:
        checkX = 0
        while checkX < bWidth:
            #if this square is not flagged and a mine, return false
            if bottomBoard[checkY][checkX] == '*' and topBoard[checkY][checkX] != 'F':
                return False
            #if this square is flagged, and is not a mine, return false
            if topBoard[checkY][checkX] == 'F' and bottomBoard[checkY][checkX] != '*':
                return False

            checkX += 1

        checkY += 1

    #if we haven't seen any discrepancies, then return true
    return True

#this function checks to see if we've removed every single hidden square that isn't a mine
def checkWin2(topBoard, bottomBoard, bWidth, bHeight, numMines):
    checkY = 0
    while checkY < bHeight:
        checkX = 0
        while checkX < bWidth:
            #if this square is hidden and NOT a mine, then return false
            if topBoard[checkY][checkX] == 'x' and bottomBoard[checkY][checkX] != '*':
                return False
            
            checkX += 1
        checkY += 1

    #otherwise, return true
    return True