from values import width, height
class game:
    def __init__(self):
        self.__x_co = 0
        self.__y_co= 0
        self.__x_velocity = 0
        self.__y_velocity = 0
        self.__noBalls = 1
        self.__noPowerUps = 0
        self.powerUpsArray = []
        self.balls = []
        self.toRemove = []
        self.__noLives = 10
        self.level = 0
        self.ufoStructure = ['$']
        self.ufoSize = 10
        self.ufoHealth = 25
        self.levelsecurity = 0
        self.bombsArray = []
        self.a3 = 0
        self.UY = 0
    def getNoLives(self):
        return self.__noLives
    def setNoLives(self, x):
        if(x <= 10):
            self.__noLives = x
    def getx(self):
        return self.__x_co
    def gety(self):
        return self.__y_co
    def setx(self, x):
        self.__x_co = x
    def sety(self, y):
        self.__y_co = y

    def getx_velocity(self):
        return self.__x_velocity
    def gety_velocity(self):
        return self.__y_velocity
    def setx_velocity(self, x):
        self.__x_velocity = x
    def sety_velocity(self, y):
        self.__y_velocity = y

    def move(self):
        self.setx(self.getx() + self.getx_velocity())
        self.sety(self.gety() + self.gety_velocity())
        
    def getNoBalls(self):
        return len(self.balls)
    def setNoBalls(self, n):
        self.__noBalls = len(self.balls)

    def getNoPowerups(self):
        return self.__noPowerUps
    def setNoPowerUps(self, n):
        self.__noPowerUps = n
    def removePowerUp(self, array):
        for i in array:
            self.powerUpsArray.remove(i) 
    def removeBalls(self):
        for i in self.toRemove:
            self.balls.remove(i)
        self.toRemove = []
    def showUfo(self,board, y):
        for i in range(y, min(y+self.ufoSize,width)):
            board[8][i] = self.ufoStructure[0]
    def clearUfo(self,board, y):
        
        for i in range(y, min(y+self.ufoSize,width)):
            board[8][i] = ' '
    def moveUfo(self, board, y):
        y = y-2
        if(y+self.ufoSize >= width-1):
            y = width-2-self.ufoSize
        if(y<=1):
            y = 1
        self.UY = y
        self.clearUfo(board, y)
        self.showUfo(board,y)
        
