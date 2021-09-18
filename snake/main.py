import time
from turtle import Screen
from food import Food
from snake import Snake
from Score import Score
# s Screen,, h Turtle, sb snake_body, l snake_length, p position, sp starting pos
#

a = 1
alive = True
s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("snake")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()
score.update()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.dw, "Down")
s.onkey(snake.rt, "Right")
s.onkey(snake.lt, "Left")

while alive:
    s.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        snake.extend()

        score.si()
        food.nf()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        snake.reset()
        score.reset()

    for seg in snake.sb[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset()
            score.reset()



s.exitonclick()

#
# detect snake collision
