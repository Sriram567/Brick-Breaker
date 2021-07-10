from input import *
from ball import *
from GameArray import *
from paddle import paddle
from brick import brick
from bricks import * 
import os
import random
from score import Score
from bomb import *
def movement():
    input = input_to(Get())
    return input
Board = screen()
Board.createScreen()
Ball = ball()
Ball.initialState()
Game.balls.append(Ball)
Paddle = paddle()
Paddle.initialState()

generateBricks()
def getBricks(board, colorboard):
    flag = 0
    for i in range(6):
        for j in range(6):
            Bricks[6*i + j].setx(Bricks[6*i + j].getx() + Bricks[6*i + j].getx_velocity())
            if(Game.level == 0):
                if(Bricks[6*i + j].strength != 0):
                    Bricks[6*i + j].clearBrick(board, colorboard, Bricks[6*i + j].getx(), Bricks[6*i + j].gety())
                    Bricks[6*i + j].showBrick(board, colorboard, Bricks[6*i + j].getx(), Bricks[6*i + j].gety())
            if(Game.level == 1):
                if( (i==0 and (j!=2 and j!=3)) or  (i==1 and (j==5 or j==0)) or (i==5 and (j!=2 and j!=3)) or  (i==4 and (j==5 or j==0)) ):
                    Bricks[6*i+j].strength = 0
                    
                if(Bricks[6*i + j].strength != 0):
                    Bricks[6*i + j].clearBrick(board, colorboard, Bricks[6*i + j].getx(), Bricks[6*i + j].gety())
                    Bricks[6*i + j].showBrick(board, colorboard, Bricks[6*i + j].getx(), Bricks[6*i + j].gety())
            if(Game.level == 2):
                if (Game.levelsecurity == 0 ):
                    if((i==3 and (j== 1 or j==3 or j==5)) or (i==4 and (j == 2 or j==4)) ):
                        Bricks[6*i+j].strength = 5
                    else:
                        Bricks[6*i+j].strength = 0
                if(Game.ufoHealth <= 18 and Game.levelsecurity == 0):
                    flag = 1
                    if(i == 5):
                        Bricks[6*i+j].strength = random.randint(1,4)
                
                if(Game.ufoHealth <=10 and Game.levelsecurity == 1):
                    flag = 1
                    if(i == 2):
                        Bricks[6*i+j].strength = random.randint(1,4)
                        
                if(Bricks[6*i + j].strength != 0):
                        Bricks[6*i + j].clearBrick(board, colorboard, Bricks[6*i + j].getx(), Bricks[6*i + j].gety())
                        Bricks[6*i + j].showBrick(board, colorboard, Bricks[6*i + j].getx(), Bricks[6*i + j].gety())
    if(flag):
        Game.levelsecurity+=1
    if(Game.levelsecurity == 1 and flag == 1):
        bb = brick(21, 6, len(Bricks))
        bb.strength = random.randint(1,4)
        Bricks.append(bb)
        bb = brick(21, 62, len(Bricks))
        bb.strength = random.randint(1,4)
        Bricks.append(bb)
        bb = brick(21, 70, len(Bricks))
        bb.strength = random.randint(1,4)
        Bricks.append(bb)
    if(Game.levelsecurity == 1):
        for ebi in range(len(Bricks)-3, len(Bricks)):
            if(Bricks[ebi].strength !=0):
                Bricks[ebi].clearBrick(board, colorboard, Bricks[ebi].getx(), Bricks[ebi].gety())
                Bricks[ebi].showBrick(board, colorboard, Bricks[ebi].getx(), Bricks[ebi].gety())
    if(Game.levelsecurity == 2 and flag == 1):
        bb = brick(12, 6, len(Bricks))
        bb.strength = random.randint(1,4)
        Bricks.append(bb)
        bb = brick(12, 62, len(Bricks))
        bb.strength = random.randint(1,4)
        Bricks.append(bb)
        bb = brick(12, 70, len(Bricks))
        bb.strength = random.randint(1,4)
        Bricks.append(bb)
    if(Game.levelsecurity == 2):
        for ebi in range(len(Bricks)-6, len(Bricks)):
            if(Bricks[ebi].strength !=0):
                Bricks[ebi].clearBrick(board, colorboard, Bricks[ebi].getx(), Bricks[ebi].gety())
                Bricks[ebi].showBrick(board, colorboard, Bricks[ebi].getx(), Bricks[ebi].gety())

    
def isGameCompleted():
    for Brick in Bricks:
        if( ( Brick.strength >=1 and Brick.strength <= 4) or Brick.strength == 6 ):
            return False
    if(Game.level!=2):
        return True 
    else:
        if(Game.ufoHealth == 0):
            return True
        else:
            return False
    
def clearScreen():
    print("\033[0;0H")
def promoteLevel():
    Game.level += 1
    Paddle.removeAllPowerUps()
    generateBricks()
    Ball =ball()
    Ball.juststated = True
    Ball.initialState()
    Game.balls = []
    Game.powerUpsArray = []
    Game.balls.append(Ball)

def quitGame():
    os.system('tput reset')
    print("GAME COMPLETED!!")
    print("Your Score is " + str(Score.finalScore()))
    quit()


    