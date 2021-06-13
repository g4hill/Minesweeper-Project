#this file is for functions that help us properly determine the mouse position

#imports
import pygame
import os
import time
import random
import numpy as np

#this function takes the mouse's position, and returns coordinates on the gameboard respective to the mouse's position
def mouseToCords(mouseCords, xOffset, yOffset):
    #gets the mouse's x and y positions (from the function parameter)
    returnX = mouseCords[0]
    returnY = mouseCords[1]

    #takes away the x and y offset
    returnX -= xOffset
    returnY -= yOffset

    #divides them by the unit size (32px)
    returnX /= 32
    returnY /= 32

    #and rounds them to get the final gameboard position
    returnX = int(returnX)
    returnY = int(returnY)

    #returns the mouse position in an array
    returnArray = [returnX, returnY]
    return returnArray

#checks to see if the mouse is on the gameboard
def isInBoard(mouseCords, xOffset, yOffset, bWidth, bHeight):
    #gets mouse x and y position
    xPos = mouseCords[0]
    yPos = mouseCords[1]

    #if the x and y mouse positions are greater than the offset values... (minimum values for being "on the board")
    if xPos > xOffset and yPos > yOffset:
        #if the x and y positions are less than the maximum x and y positions for being "on the board"...
        xMax = xOffset + bWidth * 32
        yMax = yOffset + bHeight * 32
        if xPos < xMax and yPos < yMax:
            #then the mouse is on the board
            return True
    
    #return false if the mouse isn't on the board
    return False

#detects if the mouse is in a certian range (used for detecting if we are hovering over a button when we click it)
def isInZone(mouseCords, minX, minY, maxX, maxY):
    #gets mouse x and y positions
    x = mouseCords[0]
    y = mouseCords[1]

    returner = False

    #if we're within the range set by minX, minY, maxX, and maxY, then set the returner to true
    if x >= minX:
        if x <= maxX:
            if y >= minY:
                if y <= maxY:
                    returner = True
    
    return returner