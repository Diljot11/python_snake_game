from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
            # file.write(f"{self.high_score}")

        self.goto(x=0, y=260)
        self.color('white')
        self.write(f"Score: {self.score} High Sccore: {self.high_score}", align='center', font=("Arial", 24, "normal"))
        self.hideturtle()

    def score_(self):
        self.score += 1
        if self.score>self.high_score:
            self.high_score=self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.update_score()

    def refresh(self):
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Sccore: {self.high_score}", align='center', font=("Arial", 24, "normal"))





