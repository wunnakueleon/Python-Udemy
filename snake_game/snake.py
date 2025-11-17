from turtle import Turtle, Screen
import math

screen = Screen()
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake_body()
        self.head = self.segments[0]

    def create_snake_body(self):
        for each_position in POSITION:
            self.add_segments(each_position)

    def add_segments(self, each_position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(each_position)
        self.segments.append(new_segment)

    def extend_segments(self):
       self.add_segments(self.segments[-1].position())

    def move(self):
        for each_seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[each_seg - 1].xcor()
            y_cor = self.segments[each_seg - 1].ycor()
            self.segments[each_seg].goto(x_cor, y_cor)       
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

    




