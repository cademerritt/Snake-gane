from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed(0)
        self.nf()

    def nf(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)