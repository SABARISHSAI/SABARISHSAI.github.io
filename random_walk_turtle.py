import random
from turtle import Turtle,Screen

# Initialize the turtle and screen
colors = [
    "aqua", "aquamarine", "blue", "blueviolet", "chartreuse", "coral",
    "cyan", "darkorange", "darkorchid", "darkturquoise", "deeppink",
    "deepskyblue", "dodgerblue", "fuchsia", "gold", "green", "greenyellow",
    "hotpink", "indigo", "lime", "limegreen", "magenta", "mediumaquamarine",
    "mediumorchid", "mediumpurple", "mediumseagreen", "mediumspringgreen",
    "mediumturquoise", "mediumvioletred", "orange", "orangered", "orchid",
    "pink", "plum", "purple", "red", "royalblue", "salmon", "seagreen",
    "springgreen", "steelblue", "tan", "teal", "tomato", "turquoise",
    "violet", "yellow", "yellowgreen"]


s = Turtle()
s.shape("turtle")
s.color('blue')
run = True
while run:
    moves = [1,2,3,4]
    choice = random.choice(moves)
    color = random.choice(colors)
    s.color(color)

    if choice == 1:
        s.right(90)
        distance = random.randint(10,100)
        s.forward(distance)
    if choice == 2:
        s.right(90)
        distance = random.randint(10,100)
        s.forward(distance)
    if choice == 3:
        s.left(90)
        distance = random.randint(10, 100)
        s.forward(distance)
    if choice == 4:
        s.left(90)
        distance = random.randint(10,100)
        s.forward(distance)


screen = Screen()
screen.title("HELLO")
screen.exitonclick()
