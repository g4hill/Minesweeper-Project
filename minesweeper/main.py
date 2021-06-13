#standard imports **check if we need some of these -and make sure to deal w/ numpy
import pygame
import os
import time
import random
import numpy as np

#imports for seperate files
import countAdj
import boardSetup
import drawBoard
import getAssets
import plantFlag
import mouseToCords
import unveilSpaces
import lose
import win


#sets up game window
width = 1000
height = 724
WIN = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption("minesweeper python edition")
pygame.display.set_icon(getAssets.mineSquare)


#defines the colors that we will be using later on:
RED = (255, 0, 0)
GREY = (155, 155, 155)
DRKGRY = (127, 127, 127)
DRKRGRY = (97, 97, 97)


#sets up the fonts and display text
pygame.font.init()    
titleFont = pygame.font.SysFont("comicsans", 60)
modeFont = pygame.font.SysFont("comicsans", 30)
descFont = pygame.font.SysFont("comicsans", 20)

titleLabel = titleFont.render("minesweeper(!)", 1, RED)

ezLabel = modeFont.render("easy", 1, RED)
ezDesc = descFont.render("9x9 board, 10 mines", 1, RED)

mdLabel = modeFont.render("medium", 1, RED)
mdDesc = descFont.render("16x16 board, 40 mines", 1, RED)

hdLabel = modeFont.render("hard", 1, RED)
hdDesc = descFont.render("30x16 board, 99 mines", 1, RED)

exLabel = modeFont.render("expert", 1, RED)
exDesc = descFont.render("30x20 board, 145 mines", 1, RED)


#importing sfx
bruh = pygame.mixer.Sound(getAssets.bruhSFX)
buzzer = pygame.mixer.Sound(getAssets.blockSFX)
winSound = pygame.mixer.Sound(getAssets.winSFX)

#setting up variables used in the main menu:
#min and max y positions for the buttons - the difference between maxY and minY is what determines the button height
minY = 500
maxY = 550

#starting x position of the easy, medium, hard, and expert difficulty settings, respectivley
ezX = 100
mdX = 300
hdX = 500
exX = 700

#length of each button
buttonOffset = 180

#used for displaying the gameboard:
xOffset = 20
yOffset = 35


#setting up variables that allow us to properly control the game:
#true as long as the game is running
play = True
#true as long as we're in the main menu
runMM = True
#becomes true when we're setting up the gameboard
startup = False
#becomes true once we start playing the game
runMain = False

#starts playing the game
while play:
    #while we're in the main menu:
    while runMM:
        #for every input that pygame recives...
        for event in pygame.event.get():
            #if we're closing out of the game, then stop the game (which actually lets us close the window)
            if event.type == pygame.QUIT:
                runMM = False
                play = False
            #if it's a click...
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #... and that click is the left mouse button...
                if pygame.mouse.get_pressed()[0] == True:
                    #... and the mouse is touching the easy button, then set the correct board setup variables and run the startup code (it's the same for the following 3 elif statements, except for the medium, hard, and extreme difficulties)
                    if mouseToCords.isInZone(pygame.mouse.get_pos(), ezX, minY, ezX + buttonOffset, maxY) == True:
                        numMines = 10
                        bWidth = 9
                        bHeight = 9
                        startup = True
                    elif mouseToCords.isInZone(pygame.mouse.get_pos(), mdX, minY, mdX + buttonOffset, maxY) == True:
                        numMines = 40
                        bWidth = 16
                        bHeight = 16
                        startup = True
                    elif mouseToCords.isInZone(pygame.mouse.get_pos(), hdX, minY, hdX + buttonOffset, maxY) == True:
                        numMines = 99
                        bWidth = 30
                        bHeight = 16
                        startup = True
                    elif mouseToCords.isInZone(pygame.mouse.get_pos(), exX, minY, exX + buttonOffset, maxY) == True:
                        numMines = 145
                        bWidth = 30
                        bHeight = 20
                        startup = True

        #if we're running the startup code, then don't run main menu
        if startup == True:
            runMM = False

        #sets the color of the buttons depending on where your mouse is (if it's touching the buttons, then make them a darker shade of grey)
        if mouseToCords.isInZone(pygame.mouse.get_pos(), ezX, minY, ezX + buttonOffset, maxY) == True:
            ezColor = DRKRGRY
        else:
            ezColor = DRKGRY
        if mouseToCords.isInZone(pygame.mouse.get_pos(), mdX, minY, mdX + buttonOffset, maxY) == True:
            mdColor = DRKRGRY
        else:
            mdColor = DRKGRY
        if mouseToCords.isInZone(pygame.mouse.get_pos(), hdX, minY, hdX + buttonOffset, maxY) == True:
            hdColor = DRKRGRY
        else:
            hdColor = DRKGRY
        if mouseToCords.isInZone(pygame.mouse.get_pos(), exX, minY, exX + buttonOffset, maxY) == True:
            exColor = DRKRGRY
        else:
            exColor = DRKGRY

        #displays the background, (just a blank light grey image) the title label, each of the buttons as well as their labels
        WIN.blit(getAssets.bkg, (0, 0))
        WIN.blit(titleLabel, (60, 120))

        pygame.draw.rect(WIN, ezColor, (ezX, minY, buttonOffset, 50))
        WIN.blit(ezLabel, (ezX + 5, minY))
        WIN.blit(ezDesc, (ezX + 5, minY + 25))

        pygame.draw.rect(WIN, mdColor, (mdX, minY, buttonOffset, 50))
        WIN.blit(mdLabel, (mdX + 5, minY))
        WIN.blit(mdDesc, (mdX + 5, minY + 25))

        pygame.draw.rect(WIN, hdColor, (hdX, minY, buttonOffset, 50))
        WIN.blit(hdLabel, (hdX + 5, minY))
        WIN.blit(hdDesc, (hdX + 5, minY + 25))

        pygame.draw.rect(WIN, exColor, (exX, minY, buttonOffset, 50))
        WIN.blit(exLabel, (exX + 5, minY))
        WIN.blit(exDesc, (exX + 5, minY + 25))

        #this lets us display everything we've "blitted" onscreen
        pygame.display.flip()

    #if we're in the startup process... (note that since this is just to setup the gameboard, this can be done in 1 "turn" so we don't need the while loop)
    if startup == True:
        #sets up our gameboards - bottomBoard has the mines and mine indicators, and topBoard has all the blank squares used for hiding what's on the bottomBoard
        bottomBoard = np.array([['-']*bWidth]*bHeight)
        topBoard = np.array([['x']*bWidth]*bHeight)

        #sets up x and y positions for the home and restart buttons, since they're dependent on bWidth and bHeight, we have to set them up here
        restartX = xOffset + 32*bWidth - 32
        homeX = restartX - 32
        bottomY = yOffset + 32*bHeight + 5

        #sets up a couple of "indicator variables": (their titles should be pretty self-explanatory)
        #note that a lot of these could just be booleans (and not be inside of an array for one case) instead of integers, but having them be integers was the only way I could make them properly work with python for somme reason - I might check back on them individually later, and try to make them work as booleans, but since the program works now, I'm content with the way they are
        bottomBoardIsSetup = 0
        hasLost = 0
        hasWon = 0
        hitMine = [0]
        playedSound = False

        #printMines represents the number of remaining hidden mines we haven't flagged yet, and is what the mine counter prints out -- more on this later
        printMines = numMines


        #timer variables:
        #printTime is the variable that the timer prints out -- more on this later
        printTime = 0

        #determines that we're in the first second of gameplay
        firstSecond = True


        #tells the program to run the main gameplay next, and to skip the startup next time
        runMain = True
        startup = False

        #this is used in order to reset the timer each time we start a new game
        pygame.init()

    #while we're playing a game...
    while runMain:
        #gets the current time and converts it to seconds
        timer = pygame.time.get_ticks()
        timer /= 1000
        #if we're just starting gameplay, create a timer offset so that we can start at 0 and not continue a previous game's timer
        if firstSecond == True:
            timerOffset = pygame.time.get_ticks()
            timerOffset /= 1000
            timerOffset += 1#we add a 1 here so that printTime increments itself once a new second starts, not when a new second ends (see below)
            firstSecond = False

        #subtracts the offset from the timer
        timer -= timerOffset
        
        #increments the printTime variable if the timer is greater
        if timer >= printTime and printTime < 999 and hasLost == 0 and hasWon == 0:
            printTime += 1

        #for every input that pygame recives...
        for event in pygame.event.get():
            #if we're closing out of the game, then stop the gameplay like in the main menu
            if event.type == pygame.QUIT:
                runMain = False
                play = False
            #if it's a mouse click...
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if we haven't won or lost (i.e. the game is still running)
                if hasLost == 0 and hasWon == 0:
                    #if the mouse is on the gameboard...
                    if mouseToCords.isInBoard(pygame.mouse.get_pos(), xOffset, yOffset, bWidth, bHeight) == True:
                        #gets the mouse's x and y positions
                        mouseLocation = mouseToCords.mouseToCords(pygame.mouse.get_pos(), xOffset, yOffset)
                        mouseX = int(mouseLocation[0])
                        mouseY = int(mouseLocation[1])

                        #if it's a right click...
                        if pygame.mouse.get_pressed()[2] == True:
                            #if we've clicked on a blank space, place a flag at wherever we've clicked, and deccrease the printMines variable by 1
                            if topBoard[mouseY][mouseX] == 'x':
                                plantFlag.plantFlag(topBoard, bWidth, bHeight, mouseX, mouseY)
                                printMines -= 1
                            #if we've clicked on a flag, then take the flag away, and increase the printMines variable by 1
                            elif topBoard[mouseY][mouseX] == 'F':
                                plantFlag.plantBlock(topBoard, bWidth, bHeight, mouseX, mouseY)
                                printMines += 1
                        
                        #if it's the middle mosue button, (i.e. the scroll wheel) then reveal all adjacent non-flag spaces if possible
                        elif pygame.mouse.get_pressed()[1] == True:
                            unveilSpaces.unveilMidClick(topBoard, bottomBoard, mouseX, mouseY, bWidth, bHeight, hitMine, buzzer)

                        #if it's a left click...
                        elif pygame.mouse.get_pressed()[0] == True:
                            #if we haven't set up the gameboard...
                            if bottomBoardIsSetup == 0:
                                #then set up the gameboard, and say that we've done so
                                boardSetup.setup(bottomBoard, bWidth, bHeight, numMines, mouseX, mouseY)
                                bottomBoardIsSetup = 1

                                #and reveal all the spaces that we can
                                unveilSpaces.unveilAdj(bottomBoard, topBoard, mouseX, mouseY, bWidth, bHeight)
                            #if we're clicking on a space that is a blank space on the bottom board and is unrevealed on the top board, run the unveilAdj code
                            if bottomBoard[mouseY][mouseX] == '-':
                                if topBoard[mouseY][mouseX] == 'x':
                                    unveilSpaces.unveilAdj(bottomBoard, topBoard, mouseX, mouseY, bWidth, bHeight)
                            #otherwise, reveal the space we've clicked on, and any other spaces that can be revealed because of the space we've clicked on
                            else:
                                unveilSpaces.unveilSpace(topBoard, bottomBoard, mouseX, mouseY, bWidth, bHeight, hitMine)

                #if we've clicked the left mouse button REGARDLESS of wether we're still playing the game or not,
                if pygame.mouse.get_pressed()[0] == True:
                    #if we've clicked on the home button, then run the main menu again
                    if mouseToCords.isInZone(pygame.mouse.get_pos(), homeX, bottomY, homeX + 32, bottomY + 32) == True:
                        runMM = True
                        runMain = False
                    #if we've clicked on the restart button, then restart the game with the current board type
                    elif mouseToCords.isInZone(pygame.mouse.get_pos(), restartX, bottomY, restartX + 32, bottomY + 32):
                        startup = True
                        runMain = False

        #if we've hit a mine...
        if hitMine[0] == 1:
            #set up the boards to show all remaining hidden mines
            lose.setUpLoss(topBoard, bottomBoard, bWidth, bHeight)
            #confirm that we've lost
            hasLost = 1
            #play the lose sound effect if we haven't already
            if playedSound == False:
                bruh.play()
                playedSound = True

        #if we've flagged a number of spaces equal to the number of mines on the board...
        if printMines == 0:
            #if we've flagged all the mines...
            if win.checkWin(bottomBoard, topBoard, bWidth, bHeight) == True:
                #confirm that we've won
                hasWon = 1
                #play the win sound effect if we haven't already
                if playedSound == False:
                    winSound.play()
                    playedSound = True
        #we can also win if we've clicked on all the spaces that aren't mines, (without nessecarily flagging all the mines) so I've included that in here too
        if win.checkWin2(topBoard, bottomBoard, bWidth, bHeight, numMines) == True:
            #confirm that we've won
            hasWon = 1
            #play the win sound effect if we haven't already
            if playedSound == False:
                winSound.play()
                playedSound = True
        #draws everything, and displays it onscreen
        drawBoard.drawBoard(topBoard, bottomBoard, bHeight, bWidth, xOffset, yOffset, WIN, printTime, printMines, hasWon, hasLost, restartX, homeX, bottomY)
        pygame.display.flip()

#once we're out of the play loop, quit the game and finish the program
pygame.QUIT()