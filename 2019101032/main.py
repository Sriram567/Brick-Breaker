# The whole code runs from here

from utility import *
from score import Score
COUNTER = [0, 0 ,0]
os.system('clear')
BrickChange = [0, 0 ,0]
while True:
    input = movement()
    clearScreen() 
    # if(COUNTER%50 == 0):
    #     os.system("clear")
    
    Board.createScreen()
    if(isGameCompleted()):
        if(Game.level ==  2):
            quitGame()
            
        else:
            promoteLevel()

    COUNTER[Game.level] += 1
    if(COUNTER[Game.level] >= 200):
        BrickChange[Game.level] = 1
        
    print("level - "+str(Game.level) )
    print("Red are Unbreakable! " + "Cyan are Lucky")
    print("Score - " + str(Score.calculateScore()) + "   Time - " + str(COUNTER[Game.level]//10) + " Lives - " + str(Game.getNoLives()) + "   ||| " )
    
    if(Paddle.isBullets):
        print( "TIme remaining for Bullet power up : " + str(200-Paddle.bulletsTime) + " || " )
    else:
        print("                                                                                       ")    
    if(Game.level == 2):
        print("UFO Health Bar-", end = '')
        print(Style.RESET_ALL,end="")
        for i in range(Game.ufoHealth):
            print(Fore.GREEN + Back.WHITE + "X", end='')
        for i in range(25-Game.ufoHealth):
            print(Fore.RED + Back.WHITE + ".", end='')
        print('')
    else:
        print("")

    if(Game.getNoBalls() == 0):
        newBall = ball()
        newBall.initialState()
        Game.balls.append(newBall)
    getBricks(Board.grid, Board.colorgrid)
    Ufoy = 0
    for i in range(Game.getNoBalls()):
        
        if(Game.balls[i].juststated):
            Game.balls[i].initialState()
            Game.balls[i].canMove(input)
            Game.balls[i].move(Board.grid, Game.balls[i].getx(), Paddle.gety() + 2)
        else:
            temp = Game.balls[i].onPaddle(Board.grid, Paddle.gety(), Paddle.size,Paddle.paddleGrab)
            if not (temp):
                if not (Game.balls[i].brickCollision()):
                    Game.balls[i].isCollided(Board.grid)
            if(temp and BrickChange[Game.level]):
                for jjj in range(len(Bricks)):
                    Bricks[jjj].setx(Bricks[jjj].getx() + 1)
                    if(Bricks[jjj].getx() >= height - 3):
                        os.system('tput reset')
                        print("GAME OVER!!")
                        print("Your Score is " + str(Score.calculateScore()))
                        quit()
            if(Game.level == 2):
                Ufoy = Paddle.gety()
                Ufoy-= 2
                if(Ufoy <=1):
                    Ufoy = 1
                if(Ufoy+Game.ufoSize >= width-1):
                    Ufoy = width-2-Game.ufoSize
                vall = Game.balls[i].UfoCollison(8,Ufoy)
                if(vall):
                    Game.ufoHealth -= 1
            Game.balls[i].move(Board.grid, Game.balls[i].tomove[0], Game.balls[i].tomove[1])
    array = []
    
    for PowerUp in Game.powerUpsArray:
        if(PowerUp.getx() <= height -3):
            if(PowerUp.hitPaddle(Paddle.gety(), Paddle.size) ):
                Paddle.getPowerUp(PowerUp)
                Game.removePowerUp([PowerUp])
            else:
                PowerUp.move(Board.grid, PowerUp.getx()+ PowerUp.getx_velocity(), PowerUp.gety()+ PowerUp.gety_velocity() )
        else:
            array.append(PowerUp)
    if(Game.level == 2):
        bdr = 20
        if(Game.ufoHealth<=10):
            bdr = 10
        if(COUNTER[Game.level]%bdr == 8):
            Ufoy = Paddle.gety()
            Ufoy-= 2
            if(Ufoy <=1):
                Ufoy = 1
            if(Ufoy+Game.ufoSize >= width-1):
                Ufoy = width-2-Game.ufoSize
            Game.bombsArray.append(Bomb(Ufoy))
        for booomb in Game.bombsArray:
            if(booomb.over == 1):
                Game.bombsArray.remove(booomb)
            else:
                booomb.move(Board.grid, booomb.getx(), booomb.gety(), Paddle.gety(), Paddle.size )


    Paddle.moveBullets(Board.grid)
    #Game.removePowerUp(array)     
    Paddle.movement(Board.grid, input)
    if(Game.level == 2):
        Game.moveUfo(Board.grid,Paddle.gety())
    Game.removeBalls()
    
    Board.printScreen()