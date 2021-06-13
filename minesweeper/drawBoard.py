#this file contains all nessecary functions for drawing the gameboard

#imports
import getAssets
import pygame
import os

#creates the font needed to display the current time and number of mines
pygame.font.init()    
font = pygame.font.SysFont("comicsans", 30)

#default background color used to clear the screen when drawing a new frame
BLACK = (0, 0, 0)

def drawBoard(topBoard, bottomBoard, bHeight, bWidth, xOffset, yOffset, WIN, printTime, printMines, hasWon, hasLost, restartX, homeX, bottomY):
    #clears out the screen so that we can draw a new frame
    WIN.fill(BLACK)
    WIN.blit(getAssets.bkg, (0, 0))

    #finds the x position at the last square of the board
    startX = xOffset + 32*bWidth - 105

    #creates and draws the gametime label at startX
    timerLabel = font.render("Time: " + str(printTime), 1, (255, 0, 0))
    pygame.draw.rect(WIN, BLACK, (startX, yOffset - 30, 105, 25))
    WIN.blit(timerLabel, (startX + 5, 7))

    #creates and draws the label representing the number of mines
    mineLabel = font.render("Mines: " + str(printMines), 1, (255, 0, 0))
    pygame.draw.rect(WIN, BLACK, (xOffset, yOffset - 30, 120, 25))
    WIN.blit(mineLabel, (xOffset + 5, yOffset - 25))

    #if we've won, create and draw the 'you've won' label, and uncover all spaces that are still hidden
    if hasWon == 1:
        wonLabel = font.render("you won!", 1, ((255, 0, 0)))
        WIN.blit(wonLabel, (xOffset, bottomY))
        createWinningBoard(topBoard, bWidth, bHeight)

    #if we've lost, create and draw the 'you've lost' label
    elif hasLost == 1:
        lostLabel = font.render("you lost ;(", 1, ((255, 0, 0)))
        WIN.blit(lostLabel, (xOffset, bottomY))
    
    #draws the restart and home buttons
    WIN.blit(getAssets.restartSquare, (restartX, bottomY))
    WIN.blit(getAssets.homeSquare, (homeX, bottomY))
    
    yCount = 0
    yLoc = yOffset

    #for every y position in the board
    while yCount < bHeight:
        xCount = 0
        xLoc = xOffset

        #for every x position in the board
        while xCount < bWidth:
            #if the space on topBoard isn't hidden or a flag
            if topBoard[yCount][xCount] != 'x' and topBoard[yCount][xCount] != 'F':
                #sets a variable for the value of the square for ease of use
                boardType = bottomBoard[yCount][xCount]

                #checks to see what boardType is, and draws it according to the character value
                #note that the '-' and '/' characters both draw a blank square, but the '/' character is used for squares that have been unveiled using the unveilSpaces function
                if boardType == '-' or boardType == '/':
                    WIN.blit(getAssets.regSquare, (xLoc, yLoc))
                elif boardType == '*':
                    WIN.blit(getAssets.mineSquare, (xLoc, yLoc))
                elif boardType == '!':
                    WIN.blit(getAssets.loseMineSquare, (xLoc, yLoc))
                elif boardType == 'r':
                    WIN.blit(getAssets.misMineSquare, (xLoc, yLoc))
                elif boardType == '1':
                    WIN.blit(getAssets.oneSquare, (xLoc, yLoc))
                elif boardType == '2':
                    WIN.blit(getAssets.twoSquare, (xLoc, yLoc))
                elif boardType == '3':
                    WIN.blit(getAssets.threeSquare, (xLoc, yLoc))
                elif boardType == '4':
                    WIN.blit(getAssets.fourSquare, (xLoc, yLoc))
                elif boardType == '5':
                    WIN.blit(getAssets.fiveSquare, (xLoc, yLoc))
                elif boardType == '6':
                    WIN.blit(getAssets.sixSquare, (xLoc, yLoc))
                elif boardType == '7':
                    WIN.blit(getAssets.sevenSquare, (xLoc, yLoc))
                elif boardType == '8':
                    WIN.blit(getAssets.eightSquare, (xLoc, yLoc))

            #if the position at topBoard is a flag, then draw a flag, if the position at topBoard is a blank square, then draw a blank square
            elif topBoard[yCount][xCount] == 'F':
                WIN.blit(getAssets.flagBrick, (xLoc, yLoc))
            elif topBoard[yCount][xCount] == 'x':
                WIN.blit(getAssets.topBrick, (xLoc, yLoc))
            
            xCount += 1
            xLoc += 32
        yCount += 1
        yLoc += 32

    #finally, draw the gridlines
    drawGridlines(xOffset, yOffset, bWidth, bHeight, WIN)

#this function draws the gridlines for the board
def drawGridlines(xOffset, yOffset, bWidth, bHeight, WIN):
    xPos = xOffset - 1
    yPos = yOffset - 1
    
    #draws vertical gridlines
    xCounter = bWidth + 1
    while xCounter > 0:
        pygame.draw.rect(WIN, BLACK, (xPos, yPos, 2, bHeight*32 + 2))
        xPos += 32
        xCounter -= 1

    #draws horizontal gridlines
    yCounter = bHeight + 1
    xPos = xOffset - 1
    while yCounter > 0:
        pygame.draw.rect(WIN, BLACK, (xPos, yPos, bWidth*32 + 2, 2))
        yPos += 32
        yCounter -= 1

#this function gets rid of any remaining hidden squares once we win
def createWinningBoard(topBoard, bWidth, bHeight):
    countY = 0

    while countY < bHeight:
        countX = 0
        while countX < bWidth:
            #setting topBoard to 'o' lets the drawBoard function ignore topBoard when drawing the gameboard
            if topBoard[countY][countX] == 'x':
                topBoard[countY][countX] = 'o'

            countX += 1

        countY += 1