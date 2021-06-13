#this file contains functions related to revealing parts of the gameboard to the player

#this function reveals every possible adjacent space for a given position on the gameboard, and then calls itself for every adjacent space, ensureing that every possible space that can get revealed (i.e. reveals blank spaces, but not mines) is revealed (i.e. this function creates the big "caves" that can occur when clicking a single space)
def unveilAdj(bottomBoard, topBoard, posX, posY, bWidth, bHeight):
    #if there are spaces above the given position...
    if posY - 1 >= 0:
        #if there are spaces to the left of the given position...
        if posX - 1 >= 0:
            #if the space that is the top-left of the given position isn't a mine, then reveal it
            if bottomBoard[posY - 1][posX - 1] != '*':
                topBoard[posY - 1][posX - 1] = 'o'
                #if the top-left space is an empty space (on bottomBoard) that hasn't been fully unveiled yet, then call unveilAdj on the top-left space
                if bottomBoard[posY - 1][posX - 1] == '-':
                    bottomBoard[posY - 1][posX - 1] = '/'
                    unveilAdj(bottomBoard, topBoard, posX - 1, posY - 1, bWidth, bHeight)

        #if the space that is directly above the given position exists and isn't a mine, then reveal it, and call unveilAdj on it if applicable
        if bottomBoard[posY - 1][posX] != '*':
            topBoard[posY - 1][posX] = 'o'
            if bottomBoard[posY - 1][posX] == '-':
                bottomBoard[posY - 1][posX] = '/'
                unveilAdj(bottomBoard, topBoard, posX, posY - 1, bWidth, bHeight)
        
        #if the space that is to the top-right of the given position exists and isn't a mine, then reveal it, and call unveilAdj on it if applicable
        if posX + 1 < bWidth:
            if bottomBoard[posY - 1][posX + 1] != '*':
                topBoard[posY - 1][posX + 1] = 'o'
                if bottomBoard[posY - 1][posX + 1] == '-':
                    bottomBoard[posY - 1][posX + 1] = '/'

                    unveilAdj(bottomBoard, topBoard, posX + 1, posY - 1, bWidth, bHeight)

    #if the space that is to the left of the given position exists and isn't a mine, then reveal it, and call unveilAdj on it if applicable
    if posX - 1 >= 0:
        if bottomBoard[posY][posX - 1] != '*':
            topBoard[posY][posX - 1] = 'o'
            if bottomBoard[posY][posX - 1] == '-':
                bottomBoard[posY][posX - 1] = '/'

                unveilAdj(bottomBoard, topBoard, posX - 1, posY, bWidth, bHeight)
    
    #reveal the given position, and say that we've fully unviled (i.e. revealed all possible adjacent spaces) it if we haven't yet
    topBoard[posY][posX] = 'o'
    if bottomBoard[posY][posX] == '-':
        bottomBoard[posY][posX] = '/'

    #if the space that is to the right of the given position exists and isn't a mine, then reveal it, and call unveilAdj on it if applicable
    if posX + 1 < bWidth:
        if bottomBoard[posY][posX + 1] != '*':
            topBoard[posY][posX + 1] = 'o'
            if bottomBoard[posY][posX + 1] == '-':
                bottomBoard[posY][posX + 1] = '/'

                unveilAdj(bottomBoard, topBoard, posX + 1, posY, bWidth, bHeight)

    #if there are spaces below the given position...
    if posY + 1 < bHeight:
        #if the space that is to the top-left of the given position exists and isn't a mine, then reveal it, and call unveilAdj on it if applicable
        if posX - 1 >= 0:
            if bottomBoard[posY + 1][posX - 1] != '*':
                topBoard[posY + 1][posX - 1] = 'o'
                if bottomBoard[posY + 1][posX - 1] == '-':
                    bottomBoard[posY + 1][posX - 1] = '/'

                    unveilAdj(bottomBoard, topBoard, posX - 1, posY + 1, bWidth, bHeight)

        #if the space that is directly below the given position exists and isn't a mine, then reveal it, and call unveilAdj on it if applicable
        if bottomBoard[posY + 1][posX] != '*':
            topBoard[posY + 1][posX] = 'o'
            if bottomBoard[posY + 1][posX] == '-':
                bottomBoard[posY + 1][posX] = '/'

                unveilAdj(bottomBoard, topBoard, posX, posY + 1, bWidth, bHeight)
        
        #if the space that is directly to the top-right of the given position exists and isn't a mine, then reveal it, and call unveilAdj on it if applicable
        if posX + 1 < bWidth:
            if bottomBoard[posY + 1][posX + 1] != '*':
                topBoard[posY + 1][posX + 1] = 'o'
                if bottomBoard[posY + 1][posX + 1] == '-':
                    bottomBoard[posY + 1][posX + 1] = '/'

                    unveilAdj(bottomBoard, topBoard, posX + 1, posY + 1, bWidth, bHeight)

#unveils a single space, and calls unveilAdj on that space -- this function gets called when we click on a single space
def unveilSpace(topBoard, bottomBoard, posX, posY, bWidth, bHeight, hitMine):
    #makes sure we haven't clicked on a flag
    if topBoard[posY][posX] != 'F':
        #clear the given space on topBoard (so that we can see what's on bottomBoard)
        topBoard[posY][posX] = 'o'
        #if we've clicked on a blank or numbered space, then preform unveilAdj on that space
        if bottomBoard[posY][posX] != '-':
            unveilAdj(bottomBoard, topBoard, posX, posY, bWidth, bHeight)
        #if we have clicked on a mine, then give the current position a special sprite, and set hitMine to 1 (which makes sure we lose)
        elif bottomBoard[posY][posX] == '*':
            bottomBoard[posY][posX] = '!'
            hitMine[0] = 1          

#This function reveals (and unveils) all adjacent non-flagged squares when the player clicks on the mouse's scroll wheel there -- this helps get rid of multiple squares at once, saving the player from a lot of clicking
def unveilMidClick(topBoard, bottomBoard, posX, posY, bWidth, bHeight, hitMine, buzzer):
    #if we're mid-clicking on an unveiled space...
    if topBoard[posY][posX] == 'o':
        #if we haven't fully unveiled this space yet...
        if bottomBoard[posY][posX] != '/':
            #if the number of adjacent flags at this space equals this space's number...
            if int(bottomBoard[posY][posX]) == countFlags(topBoard, posX, posY, bWidth, bHeight):
                #if there are spaces above the space we are looking at...
                if posY - 1 >= 0:
                    #if there are spaces to the left of the space we are looking at...
                    if posX - 1 >= 0:
                        #if the space to the top-left of the space we are looking at is unrevealed, then unveil it
                        if topBoard[posY - 1][posX - 1] == 'x':
                            unveilSpace(topBoard, bottomBoard, posX - 1, posY - 1, bWidth, bHeight, hitMine)

                    #if the space directly above the space we are looking at is unrevealed, then unveil it
                    if topBoard[posY - 1][posX] == 'x':
                        unveilSpace(topBoard, bottomBoard, posX, posY - 1, bWidth, bHeight, hitMine)

                    #if there are spaces to the right of the space we are looking at...
                    if posX + 1 < bWidth:
                        #if the space to the top-right of the space we are looking at is unrevealed, then unveil it
                        if topBoard[posY - 1][posX + 1] == 'x':
                            unveilSpace(topBoard, bottomBoard, posX + 1, posY - 1, bWidth, bHeight, hitMine)

                #if there are spaces to the left of the space we are looking at...
                if posX - 1 >= 0:
                    #if the space to the left of the space we are looking at is unrevealed, then unveil it
                    if topBoard[posY][posX - 1] == 'x':
                        unveilSpace(topBoard, bottomBoard, posX - 1, posY, bWidth, bHeight, hitMine)

                #if there are spaces to the right of  the space we are looking at...
                if posX + 1 < bWidth:
                    #if the space to the right off the space we are looking at is unrevealed, then unveil it
                    if topBoard[posY][posX + 1] == 'x':
                        unveilSpace(topBoard, bottomBoard, posX + 1, posY, bWidth, bHeight, hitMine)

                #if there are spaces below the space we are looking at...
                if posY + 1 < bHeight:
                    #if there are spaces to the left of the space we are looking at...
                    if posX - 1 >= 0:
                        #if the space to the bottom-left of the space we are looking at is unrevealed, then unveil it
                        if topBoard[posY + 1][posX - 1] == 'x':
                            unveilSpace(topBoard, bottomBoard, posX - 1, posY + 1, bWidth, bHeight, hitMine)

                    #if the space directly below the space we are looking at is unrevealed, then unveil it
                    if topBoard[posY + 1][posX] == 'x':
                        unveilSpace(topBoard, bottomBoard, posX, posY + 1, bWidth, bHeight, hitMine)

                    #if there are spaces to the right of the space we are looking at...
                    if posX + 1 < bWidth:
                        #if the space to the bottom-right of the space we are looking at is unrevealed, then unveil it
                        if topBoard[posY + 1][posX + 1] == 'x':
                            unveilSpace(topBoard, bottomBoard, posX + 1, posY + 1, bWidth, bHeight, hitMine)        
            
            #if we have flagged too many or too little spaces, then play the buzzer sound effect
            else:
                buzzer.play()

#this counts the number of adjacent flag squares for a given space -- this is used in the unveilMidClick function
def countFlags(topBoard, posX, posY, bWidth, bHeight):
    numFlags = 0
    
    #if there are spaces directly above the given position...
    if posY - 1 >= 0:
        #if there are spaces to the left of the given position...
        if posX - 1 >= 0:
            #if there's a flag at the top-left position relative to the given space, then increment numFlags by 1
            if topBoard[posY - 1][posX - 1] == 'F':
                numFlags += 1
        
        #if there's a flag directly above the given space, then increment numFlags by 1
        if topBoard[posY - 1][posX] == 'F':
            numFlags += 1
        
        #if there are spaces to the right of the given position...
        if posX + 1 < bWidth:
            #if there's a flag to the top-right position relative to the given space, then increment numFlags by 1
            if topBoard[posY - 1][posX + 1] == 'F':
                numFlags += 1

    #if there are spaces to the left of the given position...
    if posX - 1 >= 0:
        #if there is a flag to the left of the given space, then increment numFlags by 1
        if topBoard[posY][posX - 1] == 'F':
            numFlags += 1

    #if there are spaces to the right of the given position...
    if posX + 1 < bWidth:
        #if there is a flag to the right of the given space, then increment numFlags by 1
        if topBoard[posY][posX + 1] == 'F':
            numFlags += 1

    #if there are spaces below the given position...
    if posY + 1 < bHeight:
        #if there are spaces to the left of the given position...
        if posX - 1 >= 0:
            #if there is a flag to the bottom-left of the given space, then increment numFlags by 1
            if topBoard[posY + 1][posX - 1] == 'F':
                numFlags += 1
        #if there is a flag directly below the given space, then increment numFlags by 1
        if topBoard[posY + 1][posX] == 'F':
            numFlags += 1
        #if there are spaces to the right of the given position...
        if posX + 1 < bWidth:
            #if there is a flag to the bottom-right of the given space, then increment numFlags by 1
            if topBoard[posY + 1][posX + 1] == 'F':
                numFlags += 1

    return numFlags