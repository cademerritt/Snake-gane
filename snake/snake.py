from turtle import Turtle
import random

ccolor = ["red", "orange", "yellow", "blue", "green", "black"]
S_P = [(0, 0), (-20, 0), (-40, 0)]
MD = 20
U = 90
D = 270
L = 180
R = 0


class Snake:

    def __init__(self):
        self.sb = []
        self.c_s()
        self.head = self.sb[0]


    def c_s(self):
        for p in S_P:
            self.add_seg(p)

    def reset(self):
        for seg in self.sb:
            seg.goto(1000, 1000)
        self.sb.clear()
        self.c_s()
        self.head = self.sb[0]

    def add_seg(self, p):
        h1 = Turtle("square")

        h1.color("white")
        h1.pu()
        h1.goto(p)
        self.sb.append(h1)
        print(p, h1)
    def extend(self):
        self.add_seg(self.sb[-1].pos())



    def move(self):
        for seg in range(len(self.sb) - 1, 0, -1):

            nx = self.sb[seg - 1].xcor()
            ny = self.sb[seg - 1].ycor()
            self.sb[seg].goto(nx, ny)
            self.head.color("white")
        self.head.fd(MD)

    def up(self):
        if self.head.heading() != D:
            self.head.seth(U)

    def dw(self):
        if self.head.heading() != U:
            self.head.seth(D)

    def rt(self):
        if self.head.heading() != L:
            self.head.seth(R)

    def lt(self):
        if self.head.heading() != R:
            self.head.seth(L)






