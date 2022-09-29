#imports turtle
import turtle as trtl
import time as ti

#creates lists
colors_main = ["red", "green", "brown", "gray"]
colors = []

painter = trtl.Turtle()

painter.speed(100)

print(colors)

'''
  #redraws car shape
painter.penup()
painter.goto(280,-40)
painter.pendown()
painter.pensize(15)
painter.left(90)
painter.circle(300,180)
painter.left(90)
painter.forward(600)

#draws left square
painter.penup()
painter.goto(-250,-50)
painter.pendown()
painter.forward(150)
painter.right(90)
painter.forward(150)
painter.right(90)
painter.forward(150)
painter.right(90)
painter.forward(150)
painter.right(90)

#draws right square
painter.penup()
painter.goto(50,-50)
painter.pendown()
painter.forward(150)
painter.right(90)
painter.forward(150)
painter.right(90)
painter.forward(150)
painter.right(90)
painter.forward(150)
painter.right(90)
'''


'''
#draws ground
painter.penup()
painter.goto(-500,-350)
painter.right(90)
painter.pendown()
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)

#ground moving
painter.penup()
painter.goto(-550,-350)
painter.pendown()
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)

painter.penup()
painter.goto(-600,-350)
painter.pendown()
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
painter.circle(150,-180)
painter.left(180)
''''''



#defines amount for time and frame
time = 10
frames = 3
'''
#loop for animation
for t in range(time): 
    frames = 3
    base_ground_location = -500,-350
    while frames > (0):
        colors.append(colors_main)
        maincolor = colors.pop()

        #redraws car shape
        painter.penup()
        painter.goto(300,-40)
        painter.pendown()
        painter.pensize(15)
        painter.left(90)
        painter.circle(300,180)
        painter.left(90)
        painter.forward(600)

        colors.pop()
        #draws ground
        painter.goto(-500,-350)
        painter.penup()
        painter.right(90)
        painter.pendown()
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)

        #ground moving
        painter.penup()
        painter.goto(-550,-350)
        painter.pendown()
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)

        painter.penup()
        painter.goto(-600,-350)
        painter.pendown()
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        painter.circle(150,-180)
        painter.left(180)
        
        
        frames = frames - (1)

        trtl.clearscreen()
























wn = trtl.Screen()
wn.mainloop()
