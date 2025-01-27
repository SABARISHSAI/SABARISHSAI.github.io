from turtle import Turtle
STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POINTS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def snake_up(self):
        if self.segments[0].heading()!=270:
            '''if self.segments[0].heading() == 180:
                self.segments[0].right(90)
                self.move()
            if self.segments[0].heading() == 0:
                self.segments[0].left(90)
                self.move()'''
            self.segments[0].setheading(90)
    def snake_down(self):
        if self.segments[0].heading()!=90:
            '''if self.segments[0].heading() == 180:
                self.segments[0].left(90)
                self.move()
            if self.segments[0].heading() == 0:
                self.segments[0].right(90)
                self.move()'''
            self.segments[0].setheading(270)
    def snake_right(self):
        if self.segments[0].heading() != 180:
            '''if self.segments[0].heading() == 90:
                self.segments[0].right(90)
                self.move()
            if self.segments[0].heading() == 270:
                self.segments[0].left(90)
                self.move()'''
            self.segments[0].setheading(0)
    def snake_left(self):
        if self.segments[0].heading() != 0:
            '''if self.segments[0].heading() == 90:
                self.segments[0].left(90)
                self.move()
            if self.segments[0].heading() == 270:
                self.segments[0].right(90)
                self.move()'''
            self.segments[0].setheading(180)