from turtle import Turtle,Screen

# Initialize the turtle and screen
s = Turtle()
s.shape("turtle")
s.color('blue')

s.left(120)
for i in range(3):
    s.forward(40)
    s.right(120)
s.penup()
s.forward(40)
s.right(120)
s.forward(40)
s.pendown()
for i in range(4,15):
    for j in range (0,i):
        s.right(360/i)
        s.forward(40)



# Keep the screen open until clicked
screen = Screen()
screen.title("HELLO")
screen.exitonclick()
