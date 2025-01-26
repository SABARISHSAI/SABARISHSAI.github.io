from turtle import Turtle,Screen


sash = Turtle()
screen = Screen()

def move_forward():
    sash.forward(3)
    sash.speed('fastest')
def turn_left():
    new_heading = sash.heading()
    sash.setheading(new_heading + 10)
    sash.speed('fastest')
def move_backward():
    sash.backward(3)
    sash.speed('fastest')
def turn_right():
    new_heading = sash.heading()
    sash.setheading(new_heading - 10)
    sash.speed('fastest')
def clear():
    sash.clear()
    sash.penup()
    sash.home()
    sash.pendown()
screen.listen()
screen.onkeypress(move_forward,'Up')
screen.onkeypress(turn_left,'Left')
screen.onkeypress(turn_right,'Right')
screen.onkeypress(move_backward,'Down')
screen.onkeypress(clear,'space')






screen.exitonclick()
