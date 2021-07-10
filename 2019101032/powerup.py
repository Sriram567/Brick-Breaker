from screen import *
import os
import random
from GameArray import *
class powerup(game):
    def __init__(self):
        super().__init__()
        self.structure = ["0"]
        self.__id = 0
        self.counter = 0
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    def picker(self):
        return random.randint(1,8)
    def showPowerUp(self, board, x, y):
        board[x][y] = self.structure[0]
    def clearPowerup(self, board, x, y):
        board[x][y] = ' '
    def move(self, board, x, y):
        self.counter += 1
        fx= x
        fy = y
        if(x>=height-2):
            fx = height-2
            Game.removePowerUp([self])
        elif(x<=1):
            fx = 2
            self.setx_velocity(0-self.getx_velocity())
        if(y>=width-2):
            fy = width-3
            self.sety_velocity(0-self.gety_velocity())
        elif(y<=1):
            fy = 2
            self.sety_velocity(0-self.gety_velocity())
            
        if(self.counter%10 ==0):
            self.setx_velocity(self.getx_velocity() + 1)
        self.setx(fx)
        self.sety(fy)
        self.clearPowerup(board, fx, fy)
        self.showPowerUp(board, fx, fy)
    def hitPaddlke(self, Paddle):

        if(self.getx() >= height -3 and (self.gety() >= Paddle.gety() and self.gety() <= Paddle.gety()+ Paddle.size - 1)):
            return True
        return False
    
    def hitPaddle(self, paddlePosition,paddleSize):
        if(self.getx_velocity() == 0):
            return False
        ab = int(self.gety() + ((abs(height-2 - self.getx())/abs(self.getx_velocity()))*self.gety_velocity()))
        if(self.getx()+ self.getx_velocity() >= height-2 and (ab >= paddlePosition and ab <=paddlePosition + paddleSize-1)):
            step =  int(self.gety() + ((abs(height-2 - self.getx())/abs(self.getx_velocity()))*self.gety_velocity())  - paddlePosition - (paddleSize//2))
            if (step < -(paddleSize//2)):
                step = -(paddleSize//2)
            elif(step > (paddleSize//2)):
                step = (paddleSize//2)
            
            return True
        else:
            return False

class expandPaddle(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["E"]
        self.setid(1)
    def powerr(self):
        self.power = ["expand"]

class shrinkPaddle(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["S"]
        self.setid(2)
def powerr(self):
        self.power = ["shrink"]
class   BallMultiplier(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["M"]
        self.setid(3)
    def powerr(self):
        self.power = ["Multiply"]
class FastBall(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["F"]
        self.setid(4)
    def powerr(self):
        self.power = ["Fast"]
class ThruBall(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["T"]
        self.setid(5)
    def powerr(self):
            self.power = ["Thru"]
class paddleGrab(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["G"]
        self.setid(6)
    def powerr(self):
        self.power = ["Grab"]
class Bullets(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["B"]
        self.setid(7)
    def powerr(self):
        self.power = ["Shoot"]
class FireBall(powerup):
    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.structure = ["F"]
        self.setid(8)
    def powerr(self):
        self.power = ["Fire"]

 