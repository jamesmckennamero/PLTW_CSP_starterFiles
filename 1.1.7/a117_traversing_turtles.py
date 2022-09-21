#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color=turtle_colors.pop()
  t.color(new_color)
  my_turtles.append(t)

# sets turtle to origin point
startx = 0
starty = 0
moving = 40
angle = 45
heading = angle


# directs where the turtle must go
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(heading) 
  t.forward(moving)
 

#	modifies starting point
  startx = t.xcor()
  starty = t.ycor()
  moving = moving + (15)
  angle = angle + (20)
  heading=(heading+45)

wn = trtl.Screen()
wn.mainloop()
