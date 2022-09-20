#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color=turtle_colors.pop()
  t.color(new_color)
  my_turtles.append(t)

# sets turtle to origin point
startx = 0
starty = 0

heading = 90

# directs where the turtle must go
for t in my_turtles:
  t.goto(startx, starty)

  t.right(heading) 
  t.forward(50)
  

#	modifies starting point
  startx = t.xcor()
  starty = t.ycor()
  heading=(heading+45)

wn = trtl.Screen()
wn.mainloop()
