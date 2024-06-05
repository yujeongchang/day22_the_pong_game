from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.move_xcor = 10
        self.move_ycor = 10
        self.speed_value = 0.1    #지연시간(main.py) -> ball speed 조절

    def move(self):
        new_xcor = self.xcor() + self.move_xcor
        new_ycor = self.ycor() + self.move_ycor
        self.penup()
        self.goto(new_xcor, new_ycor)

#bounce 동작은 움직임의 방향만 바꾸어주는 것! 움직임 자체는 move 동작에서 실행된다.
#bounce도 vertical/horizontal의 두가지 버전이 있다. (상황에 따라 적절한 바운싱이 필요함)
    def bounce_ver(self):
        self.move_ycor *= -1

    def bounce_hor(self):
        self.move_xcor *= -1
        self.speed_value *= 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_hor()
        self.speed_value = 0.1

