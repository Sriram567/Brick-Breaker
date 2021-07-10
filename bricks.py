from brick import *
from GameArray import *
from powerup import *
import random
Bricks = []

def generateBricks():
    Bricks.clear()
    for i in range(6):
        for j in range(6):
            aa = brick(6 + 3*i, 14 + 8*j, 6*i + j )
            Bricks.append(aa)
def decStrength(counter, thruBall = -1,x_vel = 1, y_vel = 0):
    if(PlayMusic):
        os.system('aplay -q ./sound_effects/glass.wav&')
    if(Bricks[counter].strength == 7 ):
        Bricks[counter].strength = random.randint(1,5)
    if(Bricks[counter].strength <= 4):
        Bricks[counter].strength -= 1
        if(Bricks[counter].strength == 0):
            if(PlayMusic):
                os.system('aplay -q ./sound_effects/Explosion.wav&')
            if(Game.level!= 2):
                generatePowerUP(counter,x_vel, y_vel)
            else:
                Game.a3+=10

    if(Bricks[counter].strength >= 6):
        if(PlayMusic):
            os.system('aplay -q ./sound_effects/Explosion.wav&')
        NeededBricks = []
        NeededBricks.append(Bricks[counter])
        while len(NeededBricks)!= 0 : 
            NeededBricks[0].strength = 0
            co_ordinates = NeededBricks[0].getAdjacentBricks()
            NeededBricks.remove(NeededBricks[0])
            for Brick in Bricks:
                for co in co_ordinates:
                    if(Brick.getx() == co[0] and Brick.gety() == co[1] and Brick.strength == 6):
                        NeededBricks.append(Brick)
            cnt = 0
            for Brick in Bricks:

                for co in co_ordinates:
                    if(Brick.getx() == co[0] and Brick.gety() == co[1] and Brick.strength != 6 and Brick.strength != 0):
                        Brick.strength = 0
                        if(Game.level!= 2):
                            generatePowerUP(cnt,x_vel, y_vel)
                        else:
                            Game.a3+=10
                        
                cnt += 1
    if(thruBall >= 100):
        if(PlayMusic):
            os.system('aplay -q ./sound_effects/Explosion.wav&')
        Bricks[counter].strength = 0  
        if(Game.level!= 2):
            generatePowerUP(counter,x_vel, y_vel)
        else:
            Game.a3+=10

def generatePowerUP(counter,x_vel, y_vel):
    origninalStrength = Bricks[counter].strength
    if( Bricks[counter].strength == 0 and origninalStrength != 6 ):
        Powerup = powerup()
        number  = Powerup.picker()
        if(number == 1):
            Powerup =  expandPaddle(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )
        elif(number == 2):
            Powerup = shrinkPaddle(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )
        elif(number == 3):
            Powerup = BallMultiplier(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )
        elif(number == 4):
            Powerup = FastBall(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )
        elif(number == 5):
            Powerup = ThruBall(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )
        elif(number == 6):
            Powerup = paddleGrab(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )
        elif(number == 7):
            Powerup = Bullets(Bricks[counter].getx() ,Bricks[counter].gety() +  3 ) 
        elif(number == 8):
            Powerup = FireBall(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )  
        else:
            Powerup = paddleGrab(Bricks[counter].getx() ,Bricks[counter].gety() +  3 )

        Powerup.setx_velocity(x_vel)
        Powerup.sety_velocity(y_vel)
        Game.setNoPowerUps(Game.getNoPowerups() + 1)
        Game.powerUpsArray.append(Powerup)    
# def isInsideAnyBick( x, y):
#     # print("x , y are " + str(x) +" "+ str(y) )
#     y = int(y)
#     for brick in Bricks:
#         print("x , y are " + str(brick.getx()) +" "+ str(brick.gety()))
#         if(brick.getx() == 21 and brick.gety() == 38):
#                 print("1." + str(x>= (brick.getx()) and x <= (brick.getx()+ 2)))
#                 print("2." + str(y>= (brick.gety()) and y <= (brick.gety()+ 7)))
#         if( x>= (brick.getx()) and x <= (brick.getx()+ 2) and y>= (brick.gety()) and y <= (brick.gety()+7)):
#             return True , x, y
#     return False , -1, -1
# generateBricks()
# print(isInsideAnyBick(22, 41))