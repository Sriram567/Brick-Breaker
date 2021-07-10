from screen import *
import os
import random
from GameArray import Game
class brick(game):
    def __init__(self,x,y, index = 2 ):
        super().__init__()
        self.structure = [['-','-','-','-','-','-','-','-'], ['!','X','X','X','X','X','X','!'], ['-','-','-','-','-','-','-','-']]
        self.randomm = [ 4, 6, 6, 6, 6 ,4 ,6, 4, 5, 5, 4, 6 ,4, 5 , 1 ,1, 5, 4 ,5, 1, 3 ,3, 1, 5, 1 ,3 ,2 ,2 ,3 ,1 ,7, 2, 7, 7 ,2 ,7 ]
        self.randomm2 = [ 4, 5, 7, 7, 5 ,4 ,5, 4, 5, 5, 4, 6 ,4, 5 , 1 ,1, 5, 4 ,5, 1, 3 ,3, 1, 5, 6 ,6 ,6 ,6 ,6 ,6 ,6, 6, 6, 6 ,6 ,6 ]
        self.strength = self.randomm[index%(len(self.randomm))]
        if(Game.level == 1):
            self.strength = self.randomm2[index%(len(self.randomm2))]
        self.setx(x)
        self.sety(y)
        self.colorState = 0
        self.rainbow = 1
    def assignColor(self):
        number = self.strength
        if(number == 0):
            return Fore.BLACK + Back.BLACK
        elif(number == 1):
            return Fore.BLACK + Back.MAGENTA
        elif(number == 2):
            return Fore.BLACK + Back.BLUE
        elif(number == 3):
            return Fore.BLACK + Back.YELLOW
        elif(number == 4):
            return Fore.BLACK + Back.GREEN
        elif(number == 5):
            return Fore.BLACK + Back.RED
        elif(number == 7):
            numm = self.rainbow
            if(numm == 0):
                return Fore.BLACK + Back.BLACK
            elif(numm == 1):
                return Fore.BLACK + Back.MAGENTA
            elif(numm == 2):
                return Fore.BLACK + Back.BLUE
            elif(numm == 3):
                return Fore.BLACK + Back.YELLOW
            elif(numm == 4):
                return Fore.BLACK + Back.GREEN
            elif(numm == 5):
                return Fore.BLACK + Back.RED
            else:
                return Fore.BLACK + Back.RED

        else:
            if(self.colorState == 0):
                
                return Fore.BLACK + Back.CYAN
            else:
                
                return Fore.BLACK + Back.BLACK

              
    def showBrick(self, board, colorgrid, x, y):
        self.rainbow = random.randint(1,5)
        self.colorState = 1 - self.colorState
        for i in range(x, min(x+3,width)):
            for j in range(y, y+8):
                board[i][j] = self.structure[i-x][j-y]
                colorgrid[i][j] = self.assignColor()    
    def clearBrick(self, board, colorgrid, x, y):
        for i in range(x, min(x+3,width)):
            for j in range(y, y+8):
                board[i][j] = ' '
                colorgrid[i][j] = Fore.BLACK+ Back.WHITE
    def getAdjacentBricks(self):
        co_ordinates = [[self.getx() + 3 , self.gety() + 8],[self.getx() - 3 , self.gety() - 8],[self.getx() + 3 , self.gety() - 8],[self.getx() - 3 , self.gety() + 8],[self.getx() + 3 , self.gety()],[self.getx() - 3 , self.gety()],[self.getx() , self.gety() + 8], [self.getx() , self.gety() - 8]]
        return co_ordinates            


    