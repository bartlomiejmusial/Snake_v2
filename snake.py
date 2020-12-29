from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        # Create 3 part snake
        self.create_snake()
        # Head of the snake
        self.head = self.snake_parts[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_part(pos)

    def add_part(self, pos):
        # Add a new part to snake
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(pos)
        self.snake_parts.append(snake_part)

    def reset(self):
        for part in self.snake_parts:
            part.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

    def extend(self):
        self.add_part(self.snake_parts[-1].position())

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)

    # Move methods (0 - East, 90 - North, 180 - West, 270 - South)
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
