from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(x=0, y=260)
        self.color('white')
        self.write(f"Score: {self.score}", align='center', font=("Arial", 24, "normal"))
        self.hideturtle()

    def score_(self):
        self.clear()
        self.score += 1

        self.write(f'Score: {self.score}', align='center', font=("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=("Arial", 24, "normal"))
