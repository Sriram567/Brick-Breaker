from screen import *
import os
from GameArray import Game 
from ball import ball
from score import Score
from bricks  import *
from bullet import *
class paddle(game):
    def __init__(self):
        super().__init__()
        self.structure = ['/', '/','/', '/','/']
        self.size = 5
        self.powerUps = []
        self.paddleGrab = 0
        self.isBullets = 0
        self.bulletsTime = 0
        self.BulletsArray = []
    def showPaddle(self, board, y):
        counter = 0
        for i in range(y, min(y+self.size,width)):
            if(counter== 0  and self.isBullets == 1):
                board[height-2][i] = '$'
            else:
                board[height-2][i] = self.structure[0]
            counter +=1
        if(self.isBullets):
        #board[height-2][y] = '$'
            board[height-2][min(y+self.size,width)-1] = '$'

    def clearPaddle(self, board, y):
        for i in range(y, min(y+self.size,width)):
            board[height - 2][i] = ' '
    def move(self, board, y, mode = 0):
        self.sety(y)
        self.clearPaddle(board, y)
        self.showPaddle(board, y)
    def initialState(self):
        self.setx(height-2)
        self.sety(width//2)
    def removePowerUp(self, PowerUp, a):
        self.powerUps.remove([PowerUp, a])
    def removeEffect(self, PowerUp):
        id = PowerUp.getid()
        if(id == 1):
            self.size -= 2
        elif(id == 2):
            self.size += 2
    
        elif id == 4 :
            for Ball in Game.balls:
                Ball.setx_velocity(Ball.getx_velocity()//2)
                Ball.setx_velocity(2*Ball.gety_velocity()//2)
        elif (id == 5):
            for Ball in Game.balls:
                Ball.mode = 0
        elif id == 6:
            self.paddleGrab = 0
        elif id == 8:
            for Ball in Game.balls:
                Ball.mode = 0
        
    def addEffect(self, PowerUp):
        id = PowerUp.getid()
        if(id == 1):
            self.size += 2
        elif(id == 2):
            if(self.size >= 3):
                self.size -= 2  
        elif(id == 3):
            array = []
            for Ball in Game.balls:
                ball2 = ball()
                ball2.setx(Ball.getx())
                ball2.sety(Ball.gety())
                ball2.setx_velocity(0-Ball.getx_velocity())
                ball2.sety_velocity(0-Ball.gety_velocity())
                ball2.juststated = False
                ball2.mode = Ball.mode
                array.append(ball2)
            for i in array:
                Game.balls.append(i)
        elif id == 4 :
            for Ball in Game.balls:
                Ball.setx_velocity(2*Ball.getx_velocity())
                Ball.setx_velocity(2*Ball.gety_velocity())
        elif (id == 5):
            for Ball in Game.balls:
                Ball.mode = 1
        elif id == 6:
            self.paddleGrab = 1
        elif id == 7:
            self.isBullets = 1
            self.bulletsTime =0
        elif id == 8:
            for Ball in Game.balls:
                Ball.mode = 2
    def removeBullets(self):
        self.isBullets = 0
        self.bulletsTime = 0
        self.BulletsArray = []
    def moveBullets(self, board):
        for B in self.BulletsArray:
            if(B.over == 1):
                self.BulletsArray.remove(B)
            else:
                B.move(board, B.getx(), B.gety())

    def updatePowerUps(self, board):
        if(self.isBullets == 1):
            self.bulletsTime += 1
            if(self.bulletsTime%10 == 4):
                self.BulletsArray.append(Bullet(self.gety()))
                self.BulletsArray.append(Bullet(self.gety() + self.size))
                if(PlayMusic):
                    os.system('aplay -q ./sound_effects/Bullet.wav&')
            
        if(self.bulletsTime >=200):
            self.removeBullets()
        for i in self.powerUps:
            i[1] += 1
            if(i[1]%10 < 1):
                i[0].setx_velocity(i[0].getx_velocity() + 1)
            if(i[1] >= 200):
                self.removeEffect(i[0])
                self.removePowerUp(i[0], i[1])
    def removeAllPowerUps(self):
        self.powerUps = []
        self.removeBullets()
        self.paddleGrab = 0
        self.size = 5
        self.initialState()
    def movement(self,grid, input):
        if(input == 'q'):
            os.system('tput reset')
            print("GAME OVER!!")
            print("Your Score is " + str(Score.calculateScore()))
            quit()
        elif(input == 'a'):
            if(self.gety() > 1):
                self.move(grid, max(1,self.gety() - 3))
        elif(input == 'd'):
            if(self.gety() < width-2-self.size):
                self.move(grid, min(width-2-self.size, self.gety() + 3))
        elif(input == 'z'):
            Game.level += 1
            Game.powerUpsArray = []
            self.removeAllPowerUps()
            generateBricks()
            Ball =ball()
            Ball.juststated = True
            Ball.initialState()
            Game.balls = []
            Game.balls.append(Ball)
            if(Game.level == 3):
                os.system('tput reset')
                print("GAME OVER!!!!")
                print("Your Score is " + str(Score.finalScore()))
                
                quit()


        else:
            self.move(grid, self.gety())
        self.updatePowerUps(grid)
    def getPowerUp(self, PowerUp):
        self.addEffect(PowerUp)
        self.powerUps.append([PowerUp, 0])
    

        