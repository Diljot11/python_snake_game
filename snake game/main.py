from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(600, 600)
# open(highscore.txt

screen.bgcolor('black')
foodii = 0
y = 0.15
screen.title('Snake game Nokia 3310 ')

screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
game = True

while game:
    screen.update()
    time.sleep(y)
    snake.move()
    if snake.head.distance(food) < 15:
        score.score_()
        foodii += 1
        if foodii % 2 == 0 and y >= 0.05:
            print('1')
            y -= 0.05
        elif foodii % 2 == 0 and y >= 0.01:
            print('2')
            y -= 0.01
        elif foodii % 2 == 0 and y < 0.01:
            print('3')
            y -= 0.001
        food.refresh()
        snake.add_size()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game = False
        # snake.segments=[]
        snake.reset()
        score.refresh()
        y = 0.15

    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 2:
            # game = False
            score.refresh()
            snake.reset()
            y = 0.15

screen.exitonclick()
