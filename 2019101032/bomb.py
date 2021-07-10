from screen import *
import os
import random
from GameArray import Game
from bricks import *
class Bomb(game):
    def __init__(self,y):
        super().__init__()
        self.sety(y)
        self.setx(8)
        self.setx_velocity(1)
        self.sety_velocity(0)
        bomb = '*'
        self.structure = [bomb]
        self.over =0
    def showBomb(self, board, x, y):
        board[x][y] = self.structure[0]
    def clearBomb(self, board, x, y):
        board[x][y] = ' '
    
    def move(self, board, x, y, paddlePosition, paddleSize):
        fx = x + self.getx_velocity()
        fy = y
        
        if(self.getx() == height -3 and self.gety() >= paddlePosition and self.gety()<= paddlePosition + paddleSize):
            Game.setNoLives(Game.getNoLives() - 1)
            self.over =1

        if(self.getx() >= height -2):
            fx = 1
            self.over = 1


        self.setx(fx)
        self.sety(fy)
        self.clearBomb(board, fx, fy)
        self.showBomb(board, fx, fy)

