from turtle import Turtle

DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            seg = Turtle('square')
            seg.penup()

            seg.color('white')
            seg.goto(x, 0)
            x -= 20
            seg.shapesize(0.7, 0.7)
            self.segments.append(seg)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.speed('fastest')
        self.head.forward(10)
        # self.head=self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(2)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(2)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(2)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(2)

    def add_size(self):
        seg = Turtle('square')
        seg.penup()
        seg.color('white')
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        seg.goto(new_x, new_y)
        seg.shapesize(0.7, 0.7)
        self.segments.append(seg)
