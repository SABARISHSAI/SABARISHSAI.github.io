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
s.pensize(15)
s.speed(10000000)
run = True
while run:
    direction = [0,90,180,270]
    choice = random.choice(direction)
    color = random.choice(colors)
    s.color(color)
    s.setheading(random.choice(direction))
    s.forward(60)


screen = Screen()
screen.title("HELLO")
screen.exitonclick()
