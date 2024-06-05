from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Arial', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Arial', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.scoreboard()

    def r_point(self):
        self.r_score += 1
        self.scoreboard()
