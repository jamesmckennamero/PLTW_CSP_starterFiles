#imports turtle
import turtle as trtl
import time as ti
painter = trtl.Turtle()
#creates lists

colors_main = ["red", "green", "black"]




painter.speed(100)


'''
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


#defines amount for time and frame
time = 10

#loop for animation
for t in range(time): 
    for colors in colors_main:
        painter.reset()
        painter.pencolor(colors)
        painter.speed(100)
        #redraws car shape
        painter.penup()
        painter.goto(300,-40)
        painter.pendown()
        painter.pensize(15)
        painter.left(90)
        painter.circle(300,180)
        painter.left(90)
        painter.forward(600)
        painter.penup()

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

        ti.sleep(0.2)
        trtl.clearscreen()
        #second iteration
        painter.penup()
        painter.goto(300,-40)
        painter.pendown()
        painter.pensize(15)
        painter.left(180)
        painter.circle(300,180)
        painter.left(90)
        painter.forward(600)
        painter.penup()

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

        #ground moving

        painter.penup()
        painter.goto(-550,-350)
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

        ti.sleep(0.2)
        painter.reset()
        trtl.clearscreen()
        painter.speed(100)
        #third iteration
        painter.penup()
        painter.goto(300,-40)
        painter.pendown()
        painter.pensize(15)
        painter.left(90)
        painter.circle(300,180)
        painter.left(90)
        painter.forward(600)
        painter.penup()

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

        painter.penup()
        painter.goto(-600,-350)
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
        painter.circle(150,-180)
        painter.left(180)
        
        trtl.clearscreen()

        























wn = trtl.Screen()
wn.mainloop()
