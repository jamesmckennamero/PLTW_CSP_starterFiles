 #   a113_square.py
#   Write code to draw a square.
import turtle as trtl

painter = trtl.Turtle()

for square in range(4):
    painter.forward(40)
    painter.right(90)
# Your code here


wn = trtl.Screen()
wn.mainloop()
