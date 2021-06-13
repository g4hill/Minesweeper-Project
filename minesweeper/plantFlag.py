#plants a flag at the given mouse positions
def plantFlag(topBoard, bWidth, bHeight, mouseX, mouseY):
    if mouseX < bWidth and mouseX >= 0:
        if mouseY < bHeight and mouseY >= 0:
           topBoard[mouseY][mouseX] = 'F'

#deletes a flag (or plants a block) at the given mouse positions
def plantBlock(topBoard, bWidth, bHeight, mouseX, mouseY):
    if mouseX < bWidth and mouseX >= 0:
        if mouseY < bHeight and mouseY >= 0:
           topBoard[mouseY][mouseX] = 'x'