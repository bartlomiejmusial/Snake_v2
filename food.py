from turtle import Turtle
from random import randint


# Class Food inherits from Turtle Class
class Food(Turtle):

    def __init__(self):
        # Turtle's init method
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(randint(55, 200), randint(55, 200), randint(55, 200))
        rand_x = randint(-270, 270)
        rand_y = randint(-270, 270)
        self.goto(rand_x, rand_y)
