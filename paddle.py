from turtle import Turtle


class Paddle(Turtle):   #paddle도 터틀의 일종으로 만들자.
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setting(position)

    def setting(self, position):
        self.goto(position)

    # def up(self):
    #     self.setheading(180)
    #     self.forward(20)
    #
    # def down(self):
    #     self.setheading(180)
    #     self.backward(20)

    def go_up(self):
        x_cor = self.xcor()
        new_ycor_up = self.ycor() + 20
        self.goto(x_cor, new_ycor_up)

    def go_down(self):
        x_cor = self.xcor()
        new_ycor_down = self.ycor() - 20
        self.goto(x_cor, new_ycor_down)