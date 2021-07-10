from screen import *
import os
from bricks import Bricks, decStrength 
from GameArray import Game
from score import Score
class ball(game):
    def __init__(self):
        super().__init__()
        self.structure = ['O']
        self.structure2 = ['@']
        fire = chr(9677)
        self.structure3 = [fire]
        self.stepss = []
        self.contacttypes = []
        self.lives = 500
        self.juststated = True
        self.tomove= []
        self.mode = 0
    def showBall(self, board, x, y):
        if(x>height-1):
            x = height-1
        for i in range(min(y,width-1), min(y+1,width)):
            if(self.mode == 0):
                board[x][i] = self.structure[0]
            elif(self.mode == 1):
                board[x][i] = self.structure2[0]
            else:
                board[x][i] = self.structure3[0]
    def clearBall(self, board, x, y):
        if(x>height-1):
            x = height-1
        for i in range(min(y,width-1), min(y+1,width)):
            board[x][i] = ' '
    def move(self, board, x, y, mode = 0):

        self.setx(x)
        self.sety(y)
        self.clearBall(board, x, y)
        self.showBall(board, x, y)
    def initialState(self):
        
        self.setx(height-3)
        self.sety((width//2) +2)
        self.setx_velocity(-1)
        self.sety_velocity(1)
    def isCollided(self, board):
        if((self.getx()+ self.getx_velocity() >= height-1 or self.getx()+ self.getx_velocity() <=0)):
            if(self.getx()+ self.getx_velocity() >= height-1):
                Game.toRemove.append(self)
                self.juststated = True
                self.tomove = [self.getx()+ self.getx_velocity(), self.gety()+ self.gety_velocity()]
            else:
                self.tomove = [1, self.gety()+ self.gety_velocity()]
            if(len(Game.balls) <= len(Game.toRemove)):
                Game.setNoLives(Game.getNoLives() - 1)
            if(Game.getNoLives() == 0):
                os.system('tput reset')
                print("GAME OVER!!")
                print("Your Score is " + str(Score.calculateScore()))
                quit()
                
            self.setx_velocity(0-self.getx_velocity())
        elif(self.gety()+ self.gety_velocity() >= width-1 or self.gety()+ self.gety_velocity() <= 0):
            if(self.gety()+ self.gety_velocity() >= width-1):    
                self.tomove = [self.getx()+self.getx_velocity() , width-2 ]
            else:
                self.tomove = [self.getx()+self.getx_velocity() , 1 ]
            self.sety_velocity(0-self.gety_velocity())
        else :
            self.tomove = [self.getx()+ self.getx_velocity(), self.gety()+ self.gety_velocity()]
    def onPaddle(self, board, paddlePosition,paddleSize, paddleGrab):
        ab = int(self.gety() + ((abs(height-2 - self.getx())/abs(self.getx_velocity()))*self.gety_velocity()))
        if(self.getx()+ self.getx_velocity() >= height-2 and (ab >= paddlePosition and ab <=paddlePosition + paddleSize-1)):
            step =  int(self.gety() + ((abs(height-2 - self.getx())/abs(self.getx_velocity()))*self.gety_velocity())  - paddlePosition - (paddleSize//2))
            if (step < -(paddleSize//2)):
                step = -(paddleSize//2)
            elif(step > (paddleSize//2)):
                step = (paddleSize//2)
            self.stepss.append(step)
            self.tomove = [ height - 3, int(self.gety() + ((abs(height-2 - self.getx())/abs(self.getx_velocity()))*self.gety_velocity()))]
            self.sety_velocity(self.gety_velocity() + step)
            self.setx_velocity(0-self.getx_velocity())
            if(paddleGrab == 1):
                self.juststated = True
            if(PlayMusic):
                os.system('aplay -q ./sound_effects/glass.wav&')
            return 1
        else:
            self.tomove = [self.getx()+ self.getx_velocity(), self.gety()+ self.gety_velocity()]
            return 0

    def isInsideUfo(self, Ufox, Ufoy,x,y):
        if( x== (Ufox)  and y>= (Ufoy) and (y) <= (Ufoy+9)):
            return True, x, y
        return False, -1, -1

    def canMove(self, input):
        if(input == ' '):
            self.juststated = False
    def isCorner(self, x,y):
        if((x - 6)%3 != 1 and (((y-14)%8 == 0) or ((y-14)%8 == 7)) ):
            return True
        return False
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
    def UfoCollison(self, Ufox, Ufoy):
        x1 = self.getx()
        x2 = self.getx_velocity() + x1
        y1 = self.gety()
        y2 = self.gety_velocity() + y1
        stepx = 1
        if(x1 > x2):
            stepx = -1

        value = False
        res_x = -1
        res_y =-1
        for i in range(x1+stepx , x2+stepx, stepx):
            y_value = ((y2-y1)/(x2-x1))*(i-x1) + y1
            value, res_x, res_y = self.isInsideUfo(Ufox, Ufoy, i, y_value)
            if(value == True):
                self.setx_velocity(0-self.getx_velocity())
                Score.a3+= 10
                return True
        return False
        
    def brickCollision(self):
        x1 = self.getx()
        x2 = self.getx_velocity() + x1
        y1 = self.gety()
        y2 = self.gety_velocity() + y1
        stepx = 1
        if(x1 > x2):
            stepx = -1

        value = False
        res_x = -1
        res_y = -1
        brick_index = -1
        for i in range(x1+stepx , x2+stepx, stepx):
            y_value = ((y2-y1)/(x2-x1))*(i-x1) + y1
            value , res_x , res_y , brick_index= self.isInsideAnyBrick(i, y_value)

            if(value == True):
                break
        if(value == True):
            if(self.mode == 1):
                decStrength(brick_index, 100, self.getx_velocity(), self.gety_velocity())
                self.tomove = [self.getx(), self.gety()]
                return True
            elif(self.mode == 2):
                decStrength(brick_index, 200, self.getx_velocity(), self.gety_velocity())
                self.tomove = [self.getx(), self.gety()]
                return True

            else:
                slope = 1 if (y2-y1)/(x2-x1) > 0 else -1
                if(self.isCorner(res_x, int(res_y))):
                    decStrength(brick_index, -1, self.getx_velocity(), self.gety_velocity())
                    if (self.gety_velocity() == 0):
                        self.sety_velocity(0-self.gety_velocity())
                        self.setx_velocity(0-self.getx_velocity())
                        res_x -= stepx
                        res_y = (((y2-y1)/(x2-x1))*(res_x-x1)) + y1
                        self.tomove = [res_x, int(res_y)]
                    else:
                    
                        points = [ [res_x+1,res_y+ 1],[res_x+1,res_y- 1],[res_x-1,res_y+ 1],[res_x-1,res_y- 1] ]
                        counter = 0
                        jarray = []
                        for point in points:
                            if(abs(((point[1]- res_y)/(point[0] - res_x)) - slope) <= 0.1 ):
                                jarray.append(counter)
                            counter += 1
                        counter = 0
                        for i in jarray:
                            points.pop(i - counter)
                            counter += 1
                        hasToReverse = True
                        aa = -1
                        bb = -1
                        for point in points:
                            rtvalue , aa , bb , cc = self.isInsideAnyBrick(point[0], point[1])
                            if(rtvalue == False):
                                aa = point[0]
                                bb = point[1]
                                hasToReverse = False
                                break
                        if(hasToReverse):
                            self.sety_velocity(0-self.gety_velocity())
                            self.setx_velocity(0-self.getx_velocity())
                            res_x -= stepx
                            res_y = (((y2-y1)/(x2-x1))*(res_x-x1)) + y1
                            self.tomove = [res_x, int(res_y)]
                            self.contacttypes.append("CornerNot")

                        else:
                            prev_x = res_x - stepx

                            prev_y = (((y2-y1)/(x2-x1))*(prev_x-x1)) + y1
                            # print("aa, bb are " + str(aa) + " " + str(bb) + " and " + " prev x, y are "+ str(prev_x)+ " "+ str(prev_y))
                            if(prev_x == aa):
                                self.setx_velocity(0-self.getx_velocity())
                            else: 
                                self.sety_velocity(0-self.gety_velocity())
                        
                            self.tomove = [prev_x, int(prev_y)]
                            self.contacttypes.append("Cornermain")

                else:   
                    decStrength(brick_index, -1,  self.getx_velocity(), self.gety_velocity())
                    if (self.gety_velocity() == 0):
                        self.sety_velocity(0-self.gety_velocity())
                        self.setx_velocity(0-self.getx_velocity())
                        res_x -= stepx
                        res_y = (((y2-y1)/(x2-x1))*(res_x-x1)) + y1
                        self.tomove = [res_x, int(res_y)]
                    else:
                    
                        points = [ [res_x+1,res_y+ 1],[res_x+1,res_y- 1],[res_x-1,res_y+ 1],[res_x-1,res_y- 1] ]
                        counter = 0
                        jarray = []
                        for point in points:
                            if( abs(((point[1]- res_y)/(point[0] - res_x)) - slope) <= 0.1 ):
                                jarray.append(counter)
                            counter += 1
                        counter = 0
                        for i in jarray:
                            points.pop(i - counter)
                            counter += 1
                        hasToReverse = True
                        aa = -1
                        bb = -1
                        self.contacttypes.append(points)  
                        for point in points:
                            rtvalue , aa , bb , cc = self.isInsideAnyBrick(point[0], point[1])
                            if not rtvalue:
                                aa = point[0]
                                bb = point[1]
                                hasToReverse = False
                                break
                            

                            
                        if (hasToReverse):
                            self.sety_velocity(0-self.gety_velocity())
                            self.contacttypes.append("No pe pe pe " + str(res_x) + " " + str(res_y))

                            res_x -= stepx
                            res_y = (((y2-y1)/(x2-x1))*(res_x-x1)) + y1
                            self.tomove = [res_x, int(res_y)]

                        else:
                            prev_x = res_x - stepx
                        
                            prev_y = (((y2-y1)/(x2-x1))*(prev_x-x1)) + y1
                            #print("aa, bb are " + str(aa) + " " + str(bb) + " and " + " prev x, y are "+ str(prev_x)+ " "+ str(prev_y))
                            if(prev_x == aa):
                                self.setx_velocity(0-self.getx_velocity())
                            else: 
                                self.sety_velocity(0-self.gety_velocity())
                            
                            self.tomove = [prev_x, int(prev_y)]
                            self.contacttypes.append("No corner")
                return True
        else:
            return False