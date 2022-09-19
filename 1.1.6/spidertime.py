#   a116_ladybug.py
import turtle as trtl
painter = trtl.Turtle()

painter.speed(100)

painter.pendown()
painter.pensize(100)
painter.circle(50)
painter.penup()
painter.goto(0,150)
painter.pendown()
painter.circle(10)
painter.penup()
painter.goto(0,0)

line = 4
length = 180
angle = 120 / line
painter.pensize(5)
counter = 0

painter.pendown()
#draw painter legs loop
while (counter < line):
  painter.goto(0,20)
  painter.pendown()
  painter.setheading(angle*counter+180)
  painter.circle(150,-90)
  painter.fillcolor("black")
  counter = counter + 1
  painter.pen()

counter = 0

while (counter < line):
  painter.goto(0,20)
  painter.pendown()
  painter.setheading(angle*counter+90)
  painter.circle(150,90)
  painter.fillcolor("black")
  counter = counter + 1
  painter.pen()

painter.goto(0,20)

painter.penup()
painter.goto(-40,200)
painter.pendown()
painter.color("green")
painter.pensize(20)
painter.circle(10)
painter.penup()
painter.goto(20,200)
painter.pendown()
painter.circle(10)

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()