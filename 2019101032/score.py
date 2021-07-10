from bricks import Bricks
from GameArray import *
class score:
    def __init__(self):
        self.__score = 0
        self.a1 = 0
        self.a2= 0
        self.a3 = 0
    def __getScore(self):
        return self.__score
    def __setScore(self, x):
        self.__score = x
    def calculateScore(self):
        if(Game.level == 0):
            self.a1 = 0
            for Brick in Bricks:
                if(Brick.strength <=0):
                    self.a1 += 10
            self.__setScore(self.a1)
            return self.__getScore()
        if(Game.level == 1):
            self.a2 = 0
            for Brick in Bricks:
                if(Brick.strength <=0):
                    self.a2 += 10
            self.__setScore(self.a1 + self.a2 - 120)
            return self.__getScore()
        if(Game.level == 2):
            
            self.__setScore(self.a1 + self.a2 + self.a3-120+ Game.a3)
            return self.__getScore()    
    def finalScore(self):
        return self.__getScore()


Score = score()