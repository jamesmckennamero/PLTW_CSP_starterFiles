#imports turtle
import turtle as trtl
painter = trtl.Turtle()
#creates lists

red = "red"
green = "green"
black = "black"
colors_main = "red", "green", "black"
colors = []


print(colors)

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
frames = 3

#loop for animation
for t in range(time): 
    frames = 3
    while frames > (0):
        colors.append(red)
        colors.append(green)
        colors.append(black)
        currentcolor = colors
        painter.reset()
        painter.speed(100)
        #redraws car shape
        painter.pencolor((currentcolor))
        painter.penup()
        painter.goto(300,-40)
        painter.pendown()
        painter.pensize(15)
        painter.left(90)
        painter.circle(300,180)
        painter.left(90)
        painter.forward(600)
        painter.penup()

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
        
        trtl.clearscreen()
        frames = frames - (1)

        























wn = trtl.Screen()
wn.mainloop()
