#   a114_nested_loops_2.py 
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

x = -200
while (x < 200): 
  x = x + 50
  y = 200
  painter.goto(x,y)
  painter.color("red")
  painter.stamp()
  while painter.ycor() < 100:
    if painter.pencolor() == red:
      painter.fillcolor(green)
      painter.color(green)
    else:
      painter.fillcolor(red)
      painter.color(red)
    painter.right(90)
    painter.forward(2 * space + 10) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1

wn = trtl.Screen()
wn.mainloop()