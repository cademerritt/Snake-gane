from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGN = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 265)
        self.hideturtle()
        self.pu()
        self.score = 0
        with open("data.txt", "r") as file:

            self.high_score = int(file.read())
        self.color("white")


    def update(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score} ", align=ALIGN, font=FONT)


    def reset(self):
        print(type(self.high_score))
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")


        self.score = 0
        self.update()



    def si(self):
        self.score += 1
        self.update()


