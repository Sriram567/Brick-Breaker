from screen import *
import os
import random
from GameArray import Game
from bricks import *
class Bullet(game):
    def __init__(self,y):
        super().__init__()
        self.sety(y)
        self.setx(height-3)
        self.setx_velocity(-1)
        self.sety_velocity(0)
        self.structure = ['^']
        self.over =0
    def showBullet(self, board, x, y):
        board[x][y] = self.structure[0]
    def clearBullet(self, board, x, y):
        board[x][y] = ' '
    def isInsideAnyBrick(self, x, y):
        # print("x , y are " + str(x) +" "+ str(y) )
        y = int(y)
        counter = 0
        for brick in Bricks:
            if brick.strength != 0 :
                if( x>= (brick.getx()) and x <= (brick.getx()+ 2) and y>= (brick.gety()) and (y) <= (brick.gety()+7)):
                    return True , x, y ,counter
            counter += 1 
        return False , -1, -1, -1
    def isInsideUfo(self, Ufox, Ufoy,x,y):
        if( x== (Ufox)  and y>= (Ufoy) and (y) <= (Ufoy+9)):
            return True, x, y
        return False, -1, -1
    def move(self, board, x, y):
        fx = x + self.getx_velocity()
        fy = y
        rtvalue, _, _, counterrr = self.isInsideAnyBrick(fx, fy)
        if(rtvalue == True):
            fx -= self.getx_velocity()
            self.over = 1
            decStrength(counterrr, -1, -1, 1)
        rtvalue, _, _ = self.isInsideUfo(8, Game.UY, fx, fy)
        if(rtvalue == True):
            fx -= self.getx_velocity()
            self.over = 1
            Game.setNoLives(0-Game.getNoLives())
        if(self.getx() <= 1):
            fx = 1
            self.over = 1


        self.setx(fx)
        self.sety(fy)
        self.clearBullet(board, fx, fy)
        self.showBullet(board, fx, fy)

