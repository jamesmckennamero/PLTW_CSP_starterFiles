#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()


line = 6
length = 90
#length = 70
angle = 360 / line
ladybug.pensize(5)
counter = 0

#draw ladybug legs loop
while (counter < line):
  ladybug.goto(0,5)
  ladybug.setheading(angle*counter)
  ladybug.forward(length)
  counter = counter + 1

ladybug.penup()
ladybug.goto(0,30)
ladybug.pendown()
# create ladybug head
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(-12,-25) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(5,25)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20+5
ypos = -55+15
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots = num_dots + 1
  xpos = (-20)
  ypos = (ypos + 30)

  # position next dots
  
  num_dot = num_dots + 1


ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()