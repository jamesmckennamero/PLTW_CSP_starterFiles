#imports turtle
import turtle as trtl

#creates lists
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
colors = ["red", "blue", "green", "orange", "purple", "gold"]

painter = trtl.Turtle()
painter.speed(100)
painter.penup()
painter.goto(300,-40)

#creates car shape
painter.pendown()
painter.pensize(15)
painter.left(90)
painter.circle(300,180)
painter.left(90)
painter.forward(600)

#defines amount for time and frame
time = 10
frames = 3




























wn = trtl.Screen()
wn.mainloop()
