#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "1.1.5/robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("1.1.5/maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

for moven in range(1):
    for first in range(2):
        for left in range(3):
            turn_left()
        for movem in range(1):
            move()
        for more_left in range(1):
            turn_left()
        for movem in range(1):
            move()
    for second in range(2):
        robot.pencolor("red")
        for left in range(3):
            turn_left()
        for movem in range(1):
            move()
        for more_left in range(1):
            turn_left()
        for movem in range(1):
            move()
#---- end robot movement 

wn.mainloop()
