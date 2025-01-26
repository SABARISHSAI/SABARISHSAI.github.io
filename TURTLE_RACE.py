import random
from turtle import Turtle,Screen

message = Turtle()
message.penup()
message.hideturtle()
message.goto(0,100)

screen = Screen()
screen.setup(500,400)
is_race_on = False
user_bet = screen.textinput("make your bet","which turtle will win the race? Enter a color : ")
colors = ["red","orange","yellow","green","blue","purple"]
users = []
y_axises = -70

for turtle_index in range(0,6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(-230,y_axises)
    y_axises += 30
    users.append(t)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in users:
        if turtle.xcor() > 230:
            is_race_on = False
            message.clear()
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                message.color("green")
                message.write(f"{user_bet} won the race! Congratulations! Your bet won.", align="center", font=("Arial", 14, "bold"))
            if winning_color!=user_bet:
                message.color("red")
                message.write(f"{winning_color} won the race! Sorry, your bet lost.", align="center", font=("Arial", 14, "bold"))

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
