# Brick-BreakerBrick-Breaker
The Game is a simulated version of DX ball game. It is terminal version of DX ball game. Destroy all the bricks without losing all the lives to win!!!

Dependencies
Coloroma
numpy
Instructions
Install all the dependencies. run python3 main.py in full screen terminal

a - to move left

d - to move right

q - to quit

z - to skip the level

Space - to release ball

Features
Initially the ball stays on the top of the paddle. The player can press Space to release the ball.
When a ball hits the paddle the direction of movement of the ball after collision with the paddle will depend on the distance from the center of the paddle and the collision point, i.e further the ball hits from the center, more the deflection.
Ball performs elastic collision with the wall.
There are different coloured with different strengths. Order of strenghts
Green > yellow > Blue > Magenta
Red colours blocks are non-breakable with normal ball.
There are some exploding bricks which when hit by ball starts the chain reaction to adjacent exploding bricks.
When a exploding brick is broken all the adjacent blocks are destroyed(horizontal , vertical, diagonal)
Upon hitting the strength of brick decreases and colours of brick also changes to represent the strength.
After hitting the brick, ball changes its direction.
After a brick is destroyed a power-up is released.
They move down with constant velocity and to attain the power-up paddle has to catch the power-up.
the power-ups are :
Expand Paddle - Increases the length of paddle by 2 units
Shrink Paddle - Decreases the length of paddle by 2 units
Ball Multiplier - The number of balls currently present in the ball will be doubled
Fast Ball - Speed of the ball increases
Thru-Ball - The ball destroys every brick which comes into contact.
Paddle Grab - The paddle grab the ball and the player can release it at will.
The effect of the power-ups stay for 5 seconds.
If similar type of power-up is captured before 5 seconds the timer will be agian 5 seconds.
Score will be calculated based upon the number of bricks broken.
Live Score, time and lives remaining is displayed on screen.
After the game ends score will be displayed on screen.
Powerups will attain the velocity of ball or bullet which ever hits it either bullet or ball.
When a brick is broken a explosion sound occurs
When a bullet fires firing sound will be produced
If the paddle collects a firebullet powerups bullets will fired from both the end of paddle.
Rainbow brick will be changing its colors , whenever a hit happens it becomes normal brick which strength equal to strength before collision.
Bullets vanishes if it touches the top wall.
Boss level first defence occurs if health fall down 18. second when fall down 10
Bricks starts falling if the time exceeds 20 seconds.
Fireball when comes into contact with a brick. It also breaks all the adjacent bricks
Fireball passes through all the bricks like thru-ball.
OOPS Concepts
Inheritance : The child classes inherits the method and attributes from the parent class to avoid redundancy of code. The objects like ball, paddle , powerup and brick are all the children of Game class. classes like expand paddle , thruball etc inherits from powerup class.
class game:
   def __init__(self):
       self.__x_co = 0
       self.__y_co= 0
   def getx(self):
       return self.__x_co
   def gety(self):
       return self.__y_co
All the child classes like ball, brick , powerup uses the above mentioned methods and attributes.

Polymorphism: The child classes uses the same function of parent class for different functionality based upon the requirements. In the class Ball and paddle I have modified the move function.
# In game class
def move(self):
       self.setx(self.getx() + self.getx_velocity())
       self.sety(self.gety() + self.gety_velocity())
#  Ball - child class of Game
   def move(self, board, x, y, mode = 0):

       self.setx(x)
       self.sety(y)
       self.clearBall(board, x, y)
       self.showBall(board, x, y)
# Paddle - child Class of Game 
   def move(self, board, y):
       self.sety(y)
       self.clearPaddle(board, y)
       self.showPaddle(board, y)
Encapsulation : Many of the variables are private. Every component on the screen is an instance of class. This instantiation encapsulates the methods and attributes of the objects. The inherited variables are protected and they are getters and setters for protected inherited variables.
def getNoLives(self):
      return self.__noLives
def setNoLives(self, x):
      if(x <= 10):
          self.__noLives = x
Abstraction : Functions like ball.brickCollision() and ball.onPaddle() hide underlying implememtation and can uses where the functionality needed. It enables the users to just use the name abstracting away the inner details. The class ball has function like brickcollision , onPaddle which abstracts away the details from end users and end users can safely use the function where they find name appropriate. Paddle has removePowerUP and addPowerUP functions.
