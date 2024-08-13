from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            snake_body = Turtle(shape="square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(x, 0)
            x -= 20
            self.segments.append(snake_body)

    def add_segment(self):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(self.segments[-1].position())
        self.segments.append(snake_body)

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[x - 1].xcor()
            new_y = self.segments[x - 1].ycor()
            self.segments[x].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
