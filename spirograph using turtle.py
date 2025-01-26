import random
import turtle
from turtle import Turtle,Screen
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

s=Turtle()
for _ in range(36):
    s.color(random.choice(rainbow_colors))
    s.speed(100)
    s.circle(50)
    s.left(10)



screen = Screen()
screen.title("HELLO")
screen.exitonclick()
