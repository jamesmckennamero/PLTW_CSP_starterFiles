#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as spider,
# a less useful variable name spider is used
spider = trtl.Turtle()

#draw spider body
spider.pensize(40)
spider.circle(20)


#spider leg configuration
line = 4
length = 90
#length = 70
angle = 120 / line
spider.pensize(5)
counter = 0

#draw spider legs loop
while (counter < line):
  spider.goto(0,20)
  spider.setheading(angle*counter -45)
  spider.forward(length)
  counter = counter + 1

counter = 0

while (counter < line):
  spider.goto(0,20)
  spider.setheading(angle*counter - 240)
  spider.forward(length)
  counter = counter + 1

spider.penup()
spider.goto(-15,55)
spider.pendown()
spider.pencolor("red")
spider.pensize(10)
spider.circle(5)

spider.penup()
spider.goto(15,55)
spider.pendown()
spider.pencolor("red")
spider.pensize(10)
spider.circle(5)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
