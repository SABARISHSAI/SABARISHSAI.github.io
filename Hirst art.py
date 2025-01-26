'''import colorgram as cg
rgb_color = []
color = cg.extract('images.jpg',30)
for col in color:
    r = col.rgb.r
    g = col.rgb.g
    b = col.rgb.b
    lis = (r,g,b)
    rgb_color.append(lis)
print(rgb_color)'''
import random
import turtle as t
rgb_color = [(246, 240, 233), (249, 234, 241), (233, 247, 237), (227, 236, 245), (239, 233, 75), (209, 161, 103), (226, 70, 133), (217, 155, 10), (176, 78, 24), (204, 136, 186), (115, 168, 236), (224, 235, 2), (79, 177, 36), (72, 98, 224), (238, 164, 193), (69, 34, 26), (51, 120, 42), (241, 53, 32), (151, 66, 140), (132, 197, 131), (188, 20, 9), (52, 101, 150), (207, 6, 52), (149, 217, 173), (155, 184, 242), (24, 95, 22), (240, 172, 162), (138, 214, 234), (84, 72, 38), (65, 42, 151)]

t.colormode(255)
s = t.Turtle()
s.penup()
s.setheading(230)
s.forward(300)
s.pendown()
s.setheading(0)
for i in range(10):
    for _ in range(10):
        s.dot(20,random.choice(rgb_color))
        s.penup()
        s.forward(50)
    s.setheading(180)
    s.forward(500)
    s.setheading(90)
    s.forward(50)
    s.setheading(0)

screen = t.Screen()
screen.exitonclick()
