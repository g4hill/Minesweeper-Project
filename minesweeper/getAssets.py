#this files is used for importing all the assets used - note that all art assets were created by me, and all sound effects are free-to-use

#imports
import pygame
import os
import pygame.mixer

#initializes pygame's mixer, which is used to import the sound assets
pygame.mixer.init()

#art imports for topBoard
topBrick = pygame.image.load(os.path.join("assets", "sprites", "top.png"))
flagBrick = pygame.image.load(os.path.join("assets", "sprites", "flag.png"))

#art imports for bottomBoard
regSquare = pygame.image.load(os.path.join("assets", "sprites", "none.png"))
mineSquare = pygame.image.load(os.path.join("assets", "sprites", "mine.png"))
loseMineSquare = pygame.image.load(os.path.join("assets", "sprites", "loseMine.png"))
misMineSquare = pygame.image.load(os.path.join("assets", "sprites", "misMine.png"))

#number art imports
oneSquare = pygame.image.load(os.path.join("assets", "sprites", "1.png"))
twoSquare = pygame.image.load(os.path.join("assets", "sprites", "2.png"))
threeSquare = pygame.image.load(os.path.join("assets", "sprites", "3.png"))
fourSquare = pygame.image.load(os.path.join("assets", "sprites", "4.png"))
fiveSquare = pygame.image.load(os.path.join("assets", "sprites", "5.png"))
sixSquare = pygame.image.load(os.path.join("assets", "sprites", "6.png"))
sevenSquare = pygame.image.load(os.path.join("assets", "sprites", "7.png"))
eightSquare = pygame.image.load(os.path.join("assets", "sprites", "8.png"))

#button art imports
homeSquare = pygame.image.load(os.path.join("assets", "sprites", "home.png"))
restartSquare = pygame.image.load(os.path.join("assets", "sprites", "restart.png"))

#imports the backrgound image
bkg = pygame.image.load(os.path.join("assets", "sprites", "bkg.png"))

#imports the sound effects
bruhSFX = pygame.mixer.Sound(os.path.join("assets", "sounds", "bruh.mp3"))
blockSFX = pygame.mixer.Sound(os.path.join("assets", "sounds", "block.mp3"))
winSFX = pygame.mixer.Sound(os.path.join("assets", "sounds", "win.mp3"))